from nacl.pwhash import str
from tornado.escape import json_decode, utf8
from tornado.gen import coroutine
from tornado.web import authenticated

from .auth import AuthHandler

class UserHandler(AuthHandler):

    @authenticated
    def get(self):
        self.set_status(200)
        self.response['username'] = self.current_user['username']
        self.write_json()

    @coroutine
    @authenticated
    def put(self):
        if self.request.body:
            body = json_decode(self.request.body)
            password = body['password']
        else:
            self.send_error(400, message='You must provide a password!')
            return

        if password is not None:
            password_hash = yield self.executor.submit(str, utf8(password))

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
