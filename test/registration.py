from concurrent.futures import ThreadPoolExecutor
from json import dumps
from motor import MotorClient
from tornado.escape import json_decode
from tornado.ioloop import IOLoop
from tornado.testing import AsyncHTTPTestCase
from tornado.web import Application

from .conf import MONGODB_HOST, MONGODB_DBNAME, WORKERS, APP_SECRETKEY_SIZE

from api.handlers.registration import RegistrationHandler

import urllib.parse

class RegistrationHandlerTest(AsyncHTTPTestCase):

    @classmethod
    def setUpClass(self):
        self.my_app = Application([(r'/registration', RegistrationHandler)])

        self.my_app.db = MotorClient(**MONGODB_HOST)[MONGODB_DBNAME]

        self.my_app.executor = ThreadPoolExecutor(WORKERS)

    def setUp(self):
        super().setUp()
        self.my_app.db.users.drop()

    def tearDown(self):
        super().tearDown()
        self.my_app.db.users.drop()

    def get_new_ioloop(self):
        return IOLoop.current()

    def get_app(self):
        return self.my_app

    def test_registration(self):
        body = {
          'email': 'testEmail',
          'password': 'testPassword',
          'displayName': 'testDisplayName'
        }
        response = self.fetch('/registration', method='POST', body=dumps(body))
        self.assertEqual(200, response.code)

        body_2 = json_decode(response.body)
        self.assertIsNotNone(body_2['email'])
        self.assertIsNotNone(body_2['displayName'])

    def test_registration_duplicate(self):
        body = {
          'email': 'testEmail',
          'password': 'testPassword',
          'displayName': 'testDisplayName'
        }
        response = self.fetch('/registration', method='POST', body=dumps(body))
        self.assertEqual(200, response.code)

        response_2 = self.fetch('/registration', method='POST', body=dumps(body))
        self.assertNotEqual(200, response_2.code)
