from tornado.escape import json_decode, utf8
from nacl.pwhash import str as nacl_str
from api.handlers.login import LoginHandler
from api.handlers.registration import RegistrationHandler
from tornado.web import Application
from tornado.gen import coroutine
from tornado.ioloop import IOLoop
from json import dumps

from .base import BaseTest


class UsingGIPTest(BaseTest):

    @classmethod
    def setUpClass(self):
        self.my_app = Application([(r'/registration', RegistrationHandler), (r'/login', LoginHandler)])
        super().setUpClass()
        self.my_app.whitelist = True

    @coroutine
    def seUpDB(self):
        yield self.get_app().db.whitelist.insert_many([{
            'email': self.usingGipEmail.lower(),
            'gamify': True,
            'usingGIP': True
        }, {
            'email': self.notUsingGipEmail.lower(),
            'gamify': True,
            'usingGIP': False
        }, {
            'email': self.legacyEmail.lower(),
            'gamify': True,
        }])


    def setUp(self):
        super().setUp()

        self.usingGipEmail = 'usingGipEmail@test.com'
        self.notUsingGipEmail = 'notUsingGipEmail@test.com'
        self.legacyEmail = 'legacyEmail@test.com'
        self.password = 'testPassword'

        IOLoop.current().run_sync(self.seUpDB)

    def test_regisiter_using_GIP(self):
        body = {
          'email': self.usingGipEmail,
          'password': self.password,
          'displayName': 'testDisplayName'
        }

        response = self.fetch('/registration', method='POST', body=dumps(body))

        body = json_decode(response.body)
        print(body)
        self.assertTrue(body['usingGIP'])

    def test_login_with_GIP(self):
        register_body = {
          'email': self.usingGipEmail,
          'password': 'testPassword',
          'displayName': 'testDisplayName'
        }

        self.fetch('/registration', method='POST', body=dumps(register_body))

        login_body = {
          'email': self.usingGipEmail,
          'password': self.password
        }

        response = self.fetch('/login', method='POST', body=dumps(login_body))
        self.assertEqual(200, response.code)

        body = json_decode(response.body)
        self.assertTrue(body['usingGIP'])

    def test_login_without_GIP(self):
        register_body = {
          'email': self.notUsingGipEmail,
          'password': 'testPassword',
          'displayName': 'testDisplayName'
        }

        response = self.fetch('/registration', method='POST', body=dumps(register_body))

        body = json_decode(response.body)
        self.assertFalse(body['usingGIP'])

        login_body = {
          'email': self.notUsingGipEmail,
          'password': self.password
        }

        response = self.fetch('/login', method='POST', body=dumps(login_body))
        self.assertEqual(200, response.code)

        body = json_decode(response.body)
        self.assertFalse(body['usingGIP'])

    def test_login_pre_GIP_whitelist(self):
        register_body = {
            'email': self.legacyEmail,
            'password': 'testPassword',
            'displayName': 'testDisplayName'
        }

        response = self.fetch('/registration', method='POST', body=dumps(register_body))

        body = json_decode(response.body)
        print(body)
        self.assertFalse(body['usingGIP'])

        login_body = {
            'email': self.legacyEmail,
            'password': self.password
        }

        response = self.fetch('/login', method='POST', body=dumps(login_body))
        self.assertEqual(200, response.code)

        body = json_decode(response.body)
        print(body)
        self.assertFalse(body['usingGIP'])