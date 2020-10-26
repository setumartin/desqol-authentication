from concurrent.futures import ThreadPoolExecutor
from json import dumps
from motor import MotorClient
from nacl.utils import random
from tornado.escape import json_decode
from tornado.gen import coroutine
from tornado.ioloop import IOLoop
from tornado.testing import AsyncHTTPTestCase
from tornado.web import Application

from .conf import MONGODB_HOST, MONGODB_DBNAME, WORKERS, WHITELIST, APP_SECRETKEY_SIZE

from api.handlers.registration import RegistrationHandler

import urllib.parse

class WhitelistTest(AsyncHTTPTestCase):

    @classmethod
    def setUpClass(self):
        self.my_app = Application([(r'/registration', RegistrationHandler)])

        self.my_app.db = MotorClient(**MONGODB_HOST)[MONGODB_DBNAME]

        self.my_app.executor = ThreadPoolExecutor(WORKERS)

        self.my_app.whitelist = True

        self.my_app.hmac_key = random(size=APP_SECRETKEY_SIZE)

    def get_new_ioloop(self):
        return IOLoop.current()

    def get_app(self):
        return self.my_app

    @coroutine
    def whitelist(self):
        yield self.get_app().db.whitelist.insert_one({
            'email': self.email
        })

    def setUp(self):
        super().setUp()
        self.get_app().db.users.drop()
        self.get_app().db.whitelist.drop()

        self.email = 'whitelistedEmail'

        IOLoop.current().run_sync(self.whitelist)

    def tearDown(self):
        super().tearDown()
        self.get_app().db.users.drop()
        self.get_app().db.whitelist.drop()

    def test_registration(self):
        body = {
          'email': self.email,
          'password': 'testPassword',
          'displayName': 'testDisplayName'
        }

        response = self.fetch('/registration', method='POST', body=dumps(body))
        self.assertEqual(200, response.code)

    def test_registration_not_whitelisted(self):
        body = {
          'email': 'notWhitelistedEmail',
          'password': 'testPassword',
          'displayName': 'testDisplayName'
        }

        response = self.fetch('/registration', method='POST', body=dumps(body))
        self.assertEqual(403, response.code)
