from time import mktime
from datetime import datetime

import tornado.gen

from .base import BaseHandler

class TokenAuthHandler(BaseHandler):

    @tornado.gen.coroutine
    def prepare(self):
        now = mktime(datetime.now().utctimetuple())

        try:
            token = self.get_argument('token')
        except tornado.web.MissingArgumentError:
            self.current_user = None
            self.set_status(400)
            self.finish()
            return

        user_dct = yield self.db.users.find_one({'token': token},
                                                {'username': 1, 'expires_in': 1})

        if not user_dct:
            self.current_user = None
            return

        if now > user_dct['expires_in']:
            self.current_user = None
            return

        self.current_user = {
            'username': user_dct['username']
        }

class CheckHandler(TokenAuthHandler):

    @tornado.web.authenticated
    def get(self):
        self.set_status(200)
