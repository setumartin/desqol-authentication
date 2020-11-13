from json import dumps
from tornado.escape import json_decode
from tornado.gen import coroutine
from tornado.ioloop import IOLoop
from tornado.web import Application

from api.handlers.registration import RegistrationHandler

from .base import BaseTest

import urllib.parse

class WhitelistTest(BaseTest):

    @classmethod
    def setUpClass(self):
        self.my_app = Application([(r'/registration', RegistrationHandler)])
        super().setUpClass()
        self.my_app.whitelist = True

    @coroutine
    def whitelist(self):
        yield self.get_app().db.whitelist.insert_one({
            'email': self.email,
            'gamify': True
        })

    def setUp(self):
        super().setUp()

        self.email = 'whitelisted@test.com'

        IOLoop.current().run_sync(self.whitelist)

    def test_registration(self):
        body = {
          'email': self.email,
          'password': 'testPassword',
          'displayName': 'testDisplayName'
        }

        response = self.fetch('/registration', method='POST', body=dumps(body))
        self.assertEqual(200, response.code)

    def test_registration_case_insensitive(self):
        body = {
          'email': self.email.swapcase(),
          'password': 'testPassword',
          'displayName': 'testDisplayName'
        }

        response = self.fetch('/registration', method='POST', body=dumps(body))
        self.assertEqual(200, response.code)

    def test_registration_not_whitelisted(self):
        body = {
          'email': 'not-whitelisted@test.com',
          'password': 'testPassword',
          'displayName': 'testDisplayName'
        }

        response = self.fetch('/registration', method='POST', body=dumps(body))
        self.assertEqual(403, response.code)
