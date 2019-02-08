import datetime
import nacl.hash
import nacl.pwhash
import time
import tornado.gen
import uuid

from .base import BaseHandler

class TokenHandler(BaseHandler):

    @tornado.gen.coroutine
    def generate_token(self, username):
        token = uuid.uuid4().hex
        token_hash = nacl.hash.blake2b(token.encode(), key=self.hmac_key)
        expires_in = datetime.datetime.now() + datetime.timedelta(hours=2)
        expires_in = time.mktime(expires_in.utctimetuple())

        token = {
            'token': token_hash.decode("utf-8"),
            'expires_in': expires_in,
        }

        yield self.db.users.update_one({'username': username},
                                       {'$set': token})

        return token

    @tornado.gen.coroutine
    def post(self):
        try:
            username = self.get_argument('username')
            password = self.get_argument('password')
        except tornado.web.MissingArgumentError:
            self.send_error(400, message='You must provide a username and password!')
            return

        user = yield self.db.users.find_one({'username': username})

        if user is None:
            self.send_error(403, message='The username and/or password is incorrect!')
            return

        try:
            yield self.executor.submit(
                nacl.pwhash.verify,
                user['password_hash'],
                tornado.escape.utf8(password)
            )
        except nacl.exceptions.InvalidkeyError:
            self.send_error(403, message='The username and/or password is incorrect!')
            return

        token = yield self.generate_token(username)

        self.set_status(200)
        self.response['token'] = token['token']
        self.response['expiresIn'] = token['expires_in']
        self.write_json()
