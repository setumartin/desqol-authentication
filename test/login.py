from concurrent.futures import ThreadPoolExecutor
from json import dumps
from motor import MotorClient
from nacl.utils import random
from tornado.escape import json_decode
from tornado.ioloop import IOLoop
from tornado.testing import AsyncHTTPTestCase
from tornado.web import Application

from .conf import MONGODB_HOST, MONGODB_DBNAME, WORKERS, APP_SECRETKEY_SIZE

from api.handlers.login import LoginHandler
from api.handlers.registration import RegistrationHandler

import urllib.parse

class LoginHandlerTest(AsyncHTTPTestCase):

    @classmethod
    def setUpClass(self):
        self.my_app = Application([
          (r'/login', LoginHandler),
          (r'/registration', RegistrationHandler)
        ])

        self.my_app.db = MotorClient(**MONGODB_HOST)[MONGODB_DBNAME]

        self.my_app.executor = ThreadPoolExecutor(WORKERS)

        self.my_app.hmac_key = random(size=APP_SECRETKEY_SIZE)

    def setUp(self):
        super().setUp()
        self.my_app.db.users.drop()

        self.email = 'testEmail'
        self.password = 'testPassword'

        body = {
          'email': self.email,
          'password': self.password,
          'displayName': 'testDisplayName'
        }
        response = self.fetch('/registration', method='POST', body=dumps(body))

    def tearDown(self):
        super().tearDown()
        self.my_app.db.users.drop()

    def get_new_ioloop(self):
        return IOLoop.current()

    def get_app(self):
        return self.my_app

    def test_login(self):
        body = {
          'email': self.email,
          'password': self.password
        }

        response = self.fetch('/login', method='POST', body=dumps(body))
        self.assertEqual(200, response.code)

        body_2 = json_decode(response.body)
        self.assertIsNotNone(body_2['token'])
        self.assertIsNotNone(body_2['expiresIn'])

    def test_login_wrong_username(self):
        body = {
          'email': 'wrongUsername',
          'password': self.password
        }

        response = self.fetch('/login', method='POST', body=dumps(body))
        self.assertEqual(403, response.code)

    def test_login_wrong_password(self):
        body = {
          'email': self.email,
          'password': 'wrongPassword'
        }

        response = self.fetch('/login', method='POST', body=dumps(body))
        self.assertEqual(403, response.code)