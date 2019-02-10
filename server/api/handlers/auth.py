from datetime import datetime
from time import mktime
from tornado.gen import coroutine

from .base import BaseHandler

class AuthHandler(BaseHandler):

    @coroutine
    def prepare(self):
        super(AuthHandler, self).prepare()

        token = self.request.headers.get('X-Token')
        if token is None:
            self.current_user = None
            self.send_error(400, message='You must provide a token!')
            return

        user = yield self.db.users.find_one({
            'token': token
        }, {
            'username': 1,
            'expires_in': 1
        })

        if user is None:
            self.current_user = None
            self.send_error(403, message='Invalid token!')
            return

        current_time = mktime(datetime.now().utctimetuple())
        if current_time > user['expires_in']:
            self.current_user = None
            self.send_error(403, message='Expired token!')
            return

        self.current_user = {
            'username': user['username']
        }
