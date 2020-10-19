from concurrent.futures import ThreadPoolExecutor
from json import dumps
from motor import MotorClient
from nacl.utils import random
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
        self.my_app = Application([(r'/', RegistrationHandler)])

        self.my_app.db = MotorClient(**MONGODB_HOST)[MONGODB_DBNAME]
        self.my_app.db.users.drop()

        self.my_app.executor = ThreadPoolExecutor(WORKERS)

    @classmethod
    def tearDown(self):
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
        response = self.fetch('/',, body=dumps(body))
        self.assertEqual(200, response.code)

        body2 = json_decode(response.body)
        self.assertIsNotNone(body2['email'])
        self.assertIsNotNone(body2['displayName'])
