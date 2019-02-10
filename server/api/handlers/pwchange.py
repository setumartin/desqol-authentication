from nacl.exceptions import InvalidkeyError
from nacl.pwhash import verify, str
from tornado.escape import utf8
from tornado.gen import coroutine

from .base import BaseHandler

class PasswordChangeHandler(BaseHandler):

    @coroutine
    def post(self):
        try:
            if self.request.body:
                body = tornado.escape.json_decode(self.request.body)
                username = body['username']
                password = body['password']
            else:
              raise Exception()
        except:
            self.send_error(400, message='You must provide a username and password!')
            return

        user = yield self.db.users.find_one({'username': username})

        if user is None:
            self.send_error(403, message='The username and password are invalid!')
            return

        try:
            yield self.executor.submit(
                verify,
                user['passwordHash'],
                utf8(password)
            )
        except InvalidkeyError:
            self.send_error(403, message='The username and password are invalid!')
            return

        password_hash = yield self.executor.submit(str, utf8(password))

        yield self.db.users.update_one({
            'username': username,
        }, {
            '$set': {
                'passwordHash': password_hash
            }
        })

        self.set_status(200)
        self.write_json()
