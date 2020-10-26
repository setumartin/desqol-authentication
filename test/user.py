from concurrent.futures import ThreadPoolExecutor
from json import dumps
from motor import MotorClient
from nacl.utils import random
from tornado.escape import json_decode
from tornado.httputil import HTTPHeaders
from tornado.ioloop import IOLoop
from tornado.testing import AsyncHTTPTestCase
from tornado.web import Application

from .conf import MONGODB_HOST, MONGODB_DBNAME, WORKERS, APP_SECRETKEY_SIZE

from api.handlers.login import LoginHandler
from api.handlers.registration import RegistrationHandler
from api.handlers.user import UserHandler

import urllib.parse

class UserHandlerTest(AsyncHTTPTestCase):

    @classmethod
    def setUpClass(self):
        self.my_app = Application([
          (r'/login', LoginHandler),
          (r'/registration', RegistrationHandler),
          (r'/user', UserHandler)
        ])

        self.my_app.db = MotorClient(**MONGODB_HOST)[MONGODB_DBNAME]

        self.my_app.executor = ThreadPoolExecutor(WORKERS)

        self.my_app.hmac_key = random(size=APP_SECRETKEY_SIZE)

    def setUp(self):
        super().setUp()
        self.my_app.db.users.drop()

        self.email = 'testEmail'
        password = 'testPassword'
        self.displayName = 'testDisplayName'

        body = {
          'email': self.email,
          'password': password,
          'displayName': self.displayName
        }

        response = self.fetch('/registration', method='POST', body=dumps(body))

        body_2 = {
          'email': self.email,
          'password': password
        }

        response_2 = self.fetch('/login', method='POST', body=dumps(body_2))
        body_3 = json_decode(response_2.body)

        self.token = body_3['token']

    def tearDown(self):
        super().tearDown()
        self.my_app.db.users.drop()

    def get_new_ioloop(self):
        return IOLoop.current()

    def get_app(self):
        return self.my_app

    def test_user(self):
        headers = HTTPHeaders({'X-Token': self.token})

        response = self.fetch('/user', headers=headers)
        self.assertEqual(200, response.code)

        body_2 = json_decode(response.body)
        self.assertEqual(self.email, body_2['email'])
        self.assertEqual(self.displayName, body_2['displayName'])

    def test_user_without_token(self):
        response = self.fetch('/user')
        self.assertEqual(400, response.code)

    def test_user_wrong_token(self):
        headers = HTTPHeaders({'X-Token': 'wrongToken'})

        response = self.fetch('/user')
        self.assertEqual(400, response.code)

    def test_user_update(self):
        newDisplayName = 'newDisplayName'

        headers = HTTPHeaders({'X-Token': self.token})
        body = {
          'displayName': newDisplayName
        }

        response = self.fetch('/user', headers=headers, method='PUT', body=dumps(body))
        self.assertEqual(200, response.code)

        body_2 = json_decode(response.body)
        self.assertEqual(self.email, body_2['email'])
        self.assertEqual(newDisplayName, body_2['displayName'])
