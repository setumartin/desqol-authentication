import datetime
import nacl.pwhash
import time
import tornado.gen

from .base import BaseHandler

class AuthHandler(BaseHandler):

    @tornado.gen.coroutine
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
            'displayName': 1,
            'expiresIn': 1
        })

        if user is None:
            self.current_user = None
            self.send_error(403, message='Your token is invalid!')
            return

        now = time.mktime(datetime.datetime.now().utctimetuple())
        if now > user['expiresIn']:
            self.current_user = None
            self.send_error(403, message='Your token has expired!')
            return

        self.current_user = {
            'username': user['username'],
            'display_name': user['displayName']
        }
