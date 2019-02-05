import datetime
import time
import tornado.gen

from .base import BaseHandler

class AuthHandler(BaseHandler):

    @tornado.gen.coroutine
    def prepare(self):
        super(AuthHandler, self).prepare()

        now = time.mktime(datetime.datetime.now().utctimetuple())
        try:
            token = self.get_argument('token')
        except tornado.web.MissingArgumentError:
            self.current_user = None
            self.send_error(400, message='You must provide a token!')
            return

        user_dct = yield self.db.users.find_one({'token': token},
                                                {'username': 1, 'expires_in': 1})

        if not user_dct:
            self.current_user = None
            self.send_error(403, message='Invalid token!')
            return

        if now > user_dct['expires_in']:
            self.current_user = None
            self.send_error(403, message='Expired token!')
            return

        self.current_user = {
            'username': user_dct['username']
        }

class CheckHandler(AuthHandler):

    @tornado.web.authenticated
    def get(self):
        self.set_status(200)
        self.response['username'] = self.current_user['username']
        self.write_json()
