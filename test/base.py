from concurrent.futures import ThreadPoolExecutor
from motor import MotorClient
from nacl.utils import random
from tornado.ioloop import IOLoop
from tornado.testing import AsyncHTTPTestCase

from .conf import MONGODB_HOST, MONGODB_DBNAME, WORKERS, WHITELIST, APP_SECRETKEY_SIZE

class BaseTest(AsyncHTTPTestCase):

    @classmethod
    def setUpClass(self):
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

    def tearDown(self):
        super().tearDown()
        self.get_app().db.users.drop()
        self.get_app().db.whitelist.drop()
