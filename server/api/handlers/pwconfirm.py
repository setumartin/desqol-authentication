import nacl.pwhash
import tornado.gen

from .base import BaseHandler

class PasswordResetConfirmHandler(BaseHandler):

    @tornado.gen.coroutine
    def post(self):
        if self.request.body:
            body = tornado.escape.json_decode(self.request.body)
            token = body['token']
            password = body['password']
        else:
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
                'token': None,
                'recovery_token': None,
                'password_hash': password_hash
            }
        })

        self.set_status(200)
        self.write_json()
