from datetime import datetime
from time import mktime
from tornado.gen import coroutine

from .base import BaseHandler

class AuthHandler(BaseHandler):

    def user_has_scope(self, user, requested_scope): 
        if requested_scope is None:
            return True
        if 'scope' not in user:
            return False
        if requested_scope in user['scope']:
            return True
        return False

    @coroutine
    def prepare(self):
        super(AuthHandler, self).prepare()

        if self.request.method == 'OPTIONS':
            return

        try:
            token = self.request.headers.get('X-Token')
            if not token:
              raise Exception()
        except:
            self.current_user = None
            self.send_error(400, message='You must provide a token!')
            return

        user = yield self.db.users.find_one({
            'token': token
        }, {
            'email': 1,
            'displayName': 1,
            'expiresIn': 1,
            'scope': 1
        })

        if user is None:
            self.current_user = None
            self.send_error(403, message='Your token is invalid!')
            return

        current_time = mktime(datetime.now().utctimetuple())
        if current_time > user['expiresIn']:
            self.current_user = None
            self.send_error(403, message='Your token has expired!')
            return

        requested_scope = self.request.headers.get('X-Scope')
        if not self.user_has_scope(user, requested_scope): 
            self.current_user = None
            self.send_error(403, message='You do not have requested scope!')
            return

        self.current_user = {
            'email': user['email'],
            'display_name': user['displayName']
        }
