import nacl.hash
import nacl.pwhash
import tornado.gen
import uuid

from .base import BaseHandler

class RecoveryHandler(BaseHandler):

    @tornado.gen.coroutine
    def generate_recovery_token(self, username):
        recovery_token_uuid = uuid.uuid4().hex
        recovery_token_hash = nacl.hash.blake2b(recovery_token_uuid.encode(), key=self.hmac_key)

        recovery_token = recovery_token_hash.decode("utf-8")

        yield self.db.users.update_one({
          'username': username
        }, {
          '$set': {
            'recovery_token': recovery_token
          }
        })

        return recovery_token

    @tornado.gen.coroutine
    def get(self):
        try:
            username = self.get_argument('username')
        except tornado.web.MissingArgumentError:
            self.send_error(400, message='You must provide a username!')
            return

        user = yield self.db.users.find_one({'username': username})

        if user is None:
            self.set_status(200)
            self.response['_url'] = nil
            self.write_json()
            return

        recovery_token = yield self.generate_recovery_token(username)

        self.set_status(200)
        self.response['_token'] = recovery_token
        self.write_json()

    @tornado.gen.coroutine
    def post(self):
        try:
            token = self.get_argument('token')
            password = self.get_argument('password')
        except tornado.web.MissingArgumentError:
            self.send_error(400, message='You must provide a token and password!')
            return

        user = yield self.db.users.find_one({'recovery_token': token})

        if user is None:
            self.send_error(403, message='The token is incorrect!')
            return

        password_hash = yield self.executor.submit(
            nacl.pwhash.str,
            tornado.escape.utf8(password)
        )
        
        yield self.db.users.update_one({
            'recovery_token': token
        }, {
            '$set': {
              'recovery_token': None,
              'password_hash': password_hash
            }
        })

        self.set_status(200)
        self.write_json()
