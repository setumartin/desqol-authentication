import nacl.pwhash
import tornado.gen

from .base import BaseHandler

class SignupHandler(BaseHandler):

    @tornado.gen.coroutine
    def post(self):
        try:
            username = self.get_argument('username')
            password = self.get_argument('password')
        except tornado.web.MissingArgumentError:
            self.send_error(400, message='You must provide a username and password!')
            return

        user = yield self.db.users.find_one({'username': username})

        if user is not None:
            self.send_error(400, message='User already exists!')
            return

        password_hash = yield self.executor.submit(
            nacl.pwhash.str,
            tornado.escape.utf8(password)
        )

        yield self.db.users.insert_one({
            'username': username,
            'password_hash': password_hash
        })

        self.set_status(200)
        self.response['username'] = username
        self.write_json()
