from uuid import uuid4
from time import mktime
from datetime import datetime, timedelta

import nacl.hash
import nacl.pwhash

import tornado.gen

from .base import BaseHandler

class TokenBaseHandler(BaseHandler):

    @tornado.gen.coroutine
    def generate_token(self, username):
        token = uuid4().hex
        token_hash = nacl.hash.blake2b(token.encode(), key=self.hmac_key)
        expires_in = datetime.now() + timedelta(hours=2)
        expires_in = mktime(expires_in.utctimetuple())

        token = {
            'token': token_hash.decode("utf-8"),
            'expires_in': expires_in,
        }

        yield self.db.users.update_one({'username': username},
                                       {'$set': token})

        return token


class TokenHandler(TokenBaseHandler):

    @tornado.gen.coroutine
    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')

        user = yield self.db.users.find_one({'username': username})

        if user is None:
            self.set_status(403)
            self.finish()
            return

        try:
            yield self.executor.submit(
                nacl.pwhash.verify,
                user['password_hash'],
                tornado.escape.utf8(password)
            )
        except nacl.exceptions.InvalidkeyError:
            self.set_status(403)
            self.finish()
            return

        user_tokens = yield self.generate_token(username)
        self.write(user_tokens)
