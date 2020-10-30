from json import dumps
from nacl.pwhash import str as nacl_str
from tornado.escape import json_decode, utf8
from tornado.gen import coroutine
from tornado.httputil import HTTPHeaders
from tornado.ioloop import IOLoop
from tornado.web import Application

from api.handlers.user import UserHandler

from .base import BaseTest

import urllib.parse

class UserHandlerTest(BaseTest):

    @classmethod
    def setUpClass(self):
        self.my_app = Application([(r'/user', UserHandler)])
        super().setUpClass()

    @coroutine
    def register(self):
        password_hash = yield self.get_app().executor.submit(nacl_str, utf8(self.password))
        yield self.get_app().db.users.insert_one({
            'email': self.email,
            'passwordHash': password_hash,
            'displayName': self.display_name
        })

    @coroutine
    def login(self):
        yield self.get_app().db.users.update_one({
            'email': self.email
        }, {
            '$set': { 'token': self.token, 'expiresIn': 2147483647 }
        })

    @coroutine
    def changeScope(self):
        yield self.get_app().db.users.update_one({
            'email': self.email
        }, {
            '$set': { 'scope': self.scope}
        })

    def setUp(self):
        super().setUp()

        self.email = 'testEmail'
        self.password = 'testPassword'
        self.display_name = 'testDisplayName'
        self.token = 'testToken'
        self.scope = 'testScope'

        IOLoop.current().run_sync(self.register)
        IOLoop.current().run_sync(self.login)

    def test_user(self):
        headers = HTTPHeaders({'X-Token': self.token})

        response = self.fetch('/user', headers=headers)
        self.assertEqual(200, response.code)

        body_2 = json_decode(response.body)
        self.assertEqual(self.email, body_2['email'])
        self.assertEqual(self.display_name, body_2['displayName'])

    def test_user_without_token(self):
        response = self.fetch('/user')
        self.assertEqual(400, response.code)

    def test_user_wrong_token(self):
        headers = HTTPHeaders({'X-Token': 'wrongToken'})

        response = self.fetch('/user')
        self.assertEqual(400, response.code)

    def test_user_update(self):
        display_name_2 = 'newDisplayName'

        headers = HTTPHeaders({'X-Token': self.token})
        body = {
          'displayName': display_name_2
        }

        response = self.fetch('/user', headers=headers, method='PUT', body=dumps(body))
        self.assertEqual(200, response.code)

        body_2 = json_decode(response.body)
        self.assertEqual(self.email, body_2['email'])
        self.assertEqual(display_name_2, body_2['displayName'])

    def test_user_change_scope(self):
        headers = HTTPHeaders({'X-Token': self.token})

        response = self.fetch('/user', headers=headers)

        body = json_decode(response.body)

        self.assertEqual('', body['scope'])

        IOLoop.current().run_sync(self.changeScope)

        response = self.fetch('/user', headers=headers)

        body = json_decode(response.body)

        self.assertEqual(self.scope, body['scope'])