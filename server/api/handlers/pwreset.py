import nacl.hash
import tornado.gen
import uuid

from .base import BaseHandler

class PasswordResetHandler(BaseHandler):

    @tornado.gen.coroutine
    def generate_recovery_token(self, username):
        recovery_token_uuid = uuid.uuid4().hex
        recovery_token_hash = nacl.hash.blake2b(recovery_token_uuid.encode(), key=self.hmac_key)

        recovery_token = recovery_token_hash.decode('utf-8')

        yield self.db.users.update_one({
            'username': username
        }, {
            '$set': {
                'recoveryToken': recovery_token
            }
        })

        return recovery_token

    @tornado.gen.coroutine
    def post(self):
        try:
            if self.request.body:
                body = tornado.escape.json_decode(self.request.body)
                username = body['username']
            else:
                raise Exception()
        except:
            self.send_error(400, message='You must provide a username!')
            return

        user = yield self.db.users.find_one({'username': username})

        if user is None:
            self.set_status(200)
            self.response['_url'] = None
            self.write_json()
            return

        recovery_token = yield self.generate_recovery_token(username)

        self.set_status(200)
        self.response['_token'] = recovery_token
        self.write_json()
