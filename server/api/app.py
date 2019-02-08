import concurrent.futures
import nacl.utils
import tornado.web
import motor

from .handlers.registration import RegistrationHandler
from .handlers.login import LoginHandler
from .handlers.logout import LogoutHandler
from .handlers.user import UserHandler
from .handlers.pwreset import PasswordResetHandler
from .handlers.pwconfirm import PasswordResetConfirmHandler

from .conf import (MONGODB_HOST, MONGODB_DBNAME, APP_SECRETKEY_SIZE, WORKERS)

class Application(tornado.web.Application):

    def __init__(self):

        handlers = [
            (r'/api/registration', RegistrationHandler),
            (r'/api/login', LoginHandler),
            (r'/api/logout', LogoutHandler),
            (r'/api/user', UserHandler),
            (r'/api/password/reset', PasswordResetHandler),
            (r'/api/password/reset/confirm', PasswordResetConfirmHandler)
        ]

        settings = dict(
            login_url='/login'
        )

        super(Application, self).__init__(handlers, **settings)

        self.db = motor.MotorClient(**MONGODB_HOST)[MONGODB_DBNAME]

        self.executor = concurrent.futures.ThreadPoolExecutor(WORKERS)

        self.hmac_key = nacl.utils.random(size=APP_SECRETKEY_SIZE)
