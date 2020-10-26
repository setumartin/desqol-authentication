from concurrent.futures import ThreadPoolExecutor
from json import dumps
from motor import MotorClient
from nacl.utils import random
from tornado.escape import json_decode
from tornado.httputil import HTTPHeaders
from tornado.ioloop import IOLoop
from tornado.testing import AsyncHTTPTestCase
from tornado.web import Application

from .conf import MONGODB_HOST, MONGODB_DBNAME, WORKERS, WHITELIST, APP_SECRETKEY_SIZE

from api.handlers.login import LoginHandler
from api.handlers.logout import LogoutHandler
from api.handlers.registration import RegistrationHandler

import urllib.parse

class LogoutHandlerTest(AsyncHTTPTestCase):

    @classmethod
    def setUpClass(self):
        self.my_app = Application([
          (r'/login', LoginHandler),
          (r'/logout', LogoutHandler),
          (r'/registration', RegistrationHandler)
        ])

        self.my_app.db = MotorClient(**MONGODB_HOST)[MONGODB_DBNAME]

        self.my_app.executor = ThreadPoolExecutor(WORKERS)

        self.my_app.whitelist = WHITELIST

        self.my_app.hmac_key = random(size=APP_SECRETKEY_SIZE)

    def get_new_ioloop(self):
        return IOLoop.current()

    def get_app(self):
        return self.my_app

    def setUp(self):
        super().setUp()
        self.get_app().db.users.drop()
        self.get_app().db.whitelist.drop()

        email = 'testEmail'
        password = 'testPassword'

        body = {
          'email': email,
          'password': password,
          'displayName': 'testDisplayName'
        }

        response = self.fetch('/registration', method='POST', body=dumps(body))

        body_2 = {
          'email': email,
          'password': password
        }

        response_2 = self.fetch('/login', method='POST', body=dumps(body_2))
        body_3 = json_decode(response_2.body)

        self.token = body_3['token']

    def tearDown(self):
        super().tearDown()
        self.get_app().db.users.drop()
        self.get_app().db.whitelist.drop()

    def test_logout(self):
        headers = HTTPHeaders({'X-Token': self.token})
        body = {}

        response = self.fetch('/logout', headers=headers, method='POST', body=dumps(body))
        self.assertEqual(200, response.code)

    def test_logout_without_token(self):
        body = {}

        response = self.fetch('/logout', method='POST', body=dumps(body))
        self.assertEqual(400, response.code)

    def test_logout_wrong_token(self):
        headers = HTTPHeaders({'X-Token': 'wrongToken'})
        body = {}

        response = self.fetch('/logout', method='POST', body=dumps(body))
        self.assertEqual(400, response.code)

    def test_logout_twice(self):
        headers = HTTPHeaders({'X-Token': self.token})
        body = {}

        response = self.fetch('/logout', headers=headers, method='POST', body=dumps(body))
        self.assertEqual(200, response.code)

        response_2 = self.fetch('/logout', headers=headers, method='POST', body=dumps(body))
        self.assertEqual(403, response_2.code)
