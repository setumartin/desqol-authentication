import concurrent.futures
import nacl.utils
import tornado.web
import motor

from .handlers.check import CheckHandler
from .handlers.signup import SignupHandler
from .handlers.token import TokenHandler

from .conf import (MONGODB_HOST, MONGODB_DBNAME, APP_SECRETKEY_SIZE, WORKERS)

class Application(tornado.web.Application):

    def __init__(self):

        handlers = [
            (r'/api/signup', SignupHandler),
            (r'/api/token', TokenHandler),
            (r'/api/check', CheckHandler)
        ]

        settings = dict(
            login_url='/login'
        )

        super(Application, self).__init__(handlers, **settings)

        self.db = motor.MotorClient(**MONGODB_HOST)[MONGODB_DBNAME]

        self.executor = concurrent.futures.ThreadPoolExecutor(WORKERS)

        self.hmac_key = nacl.utils.random(size=APP_SECRETKEY_SIZE)
