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

        user = yield self.db.users.find_one({'recoveryToken': token})

        if user is None:
            self.send_error(403, message='The token is invalid!')
            return

        if not password:
            self.send_error(400, message='The password is invalid!')
            return

        password_hash = yield self.executor.submit(str, utf8(password))

        yield self.db.users.update_one({
            'recoveryToken': token
        }, {
            '$set': {
                'token': None,
                'recoveryToken': None,
                'passwordHash': password_hash
            }
        })

        self.set_status(200)
        self.write_json()
