from tornado.escape import json_decode
from tornado.ioloop import IOLoop
from tornado.testing import AsyncHTTPTestCase
from tornado.web import Application

from api.handlers.welcome import WelcomeHandler

class WelcomeHandlerTest(AsyncHTTPTestCase):

    @classmethod
    def setUpClass(self):
        self.my_app = Application([(r'/welcome', WelcomeHandler)])

    def get_new_ioloop(self):
        return IOLoop.current()

    def get_app(self):
        return self.my_app

    def test_welcome(self):
        response = self.fetch('/welcome')
        self.assertEqual(200, response.code)

        body = json_decode(response.body)
        self.assertIsNotNone(body['message'])
