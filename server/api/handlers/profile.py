import datetime
import nacl.pwhash
import time
import tornado.escape
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
            'expires_in': 1
        })

        if user is None:
            self.current_user = None
            self.send_error(403, message='Invalid token!')
            return

        now = time.mktime(datetime.datetime.now().utctimetuple())
        if now > user['expires_in']:
            self.current_user = None
            self.send_error(403, message='Expired token!')
            return

        self.current_user = {
            'username': user['username']
        }

class ProfileHandler(AuthHandler):

    @tornado.web.authenticated
    def get(self):
        self.set_status(200)
        self.response['username'] = self.current_user['username']
        self.write_json()

    @tornado.gen.coroutine
    @tornado.web.authenticated
    def put(self):
        if self.request.body:
            body = tornado.escape.json_decode(self.request.body)
            password = body['password']
        else:
            self.send_error(400, message='You must provide a password!')
            return

        if password is not None:
            password_hash = yield self.executor.submit(
                nacl.pwhash.str,
                tornado.escape.utf8(password)
            )

            yield self.db.users.update_one({
                'username': self.current_user['username'],
            }, {
                '$set': {
                    'password_hash': password_hash
                }
            })

        self.set_status(200)
        self.response['username'] = self.current_user['username']
        self.write_json()
