from nacl.pwhash import str
from tornado.escape import json_decode, utf8
from tornado.gen import coroutine

from .base import BaseHandler

class PasswordResetConfirmHandler(BaseHandler):

    @coroutine
    def post(self):
        if self.request.body:
            body = json_decode(self.request.body)
            token = body['token']
            password = body['password']
        else:
            self.send_error(400, message='You must provide a token and password!')
            return

        user = yield self.db.users.find_one({'recovery_token': token})

        if user is None:
            self.send_error(403, message='The token is incorrect!')
            return

        password_hash = yield self.executor.submit(str, utf8(password))

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
