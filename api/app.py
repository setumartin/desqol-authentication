from concurrent.futures import ThreadPoolExecutor
from nacl.utils import random
from tornado.web import Application
from motor import MotorClient

from .handlers.welcome import WelcomeHandler
from .handlers.registration import RegistrationHandler
from .handlers.login import LoginHandler
from .handlers.logout import LogoutHandler
from .handlers.user import UserHandler
from .handlers.pwreset import PasswordResetHandler
from .handlers.pwconfirm import PasswordResetConfirmHandler
from .handlers.pwchange import PasswordChangeHandler

from .conf import MONGODB_HOST, MONGODB_DBNAME, WORKERS, APP_SECRETKEY_SIZE

class Application(Application):

    def __init__(self):
        handlers = [
            (r'/desqol-auth', WelcomeHandler),
            (r'/desqol-auth/api', WelcomeHandler),
            (r'/desqol-auth/api/registration', RegistrationHandler),
            (r'/desqol-auth/api/login', LoginHandler),
            (r'/desqol-auth/api/logout', LogoutHandler),
            (r'/desqol-auth/api/user', UserHandler),
            (r'/desqol-auth/api/password/reset', PasswordResetHandler),
            (r'/desqol-auth/api/password/reset/confirm', PasswordResetConfirmHandler),
            (r'/desqol-auth/api/password/change', PasswordChangeHandler)
        ]

        settings = dict()

        super(Application, self).__init__(handlers, **settings)

        self.db = MotorClient(**MONGODB_HOST)[MONGODB_DBNAME]

        self.executor = ThreadPoolExecutor(WORKERS)

        self.hmac_key = random(size=APP_SECRETKEY_SIZE)
