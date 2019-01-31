import nacl.pwhash

import tornado.gen

from .base import BaseHandler

class SignupHandler(BaseHandler):

    @tornado.gen.coroutine
    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')

        user = yield self.db.users.find_one({'username': username})
        
        if user is not None:
            self.set_status(400)
            self.finish()
            return

        password_hash = yield self.executor.submit(
            nacl.pwhash.str,
            tornado.escape.utf8(password)
        )

        user = {
            'username': username,
            'password_hash': password_hash
        }
        yield self.db.users.insert_one(user)
        self.set_status(200)
