from nacl.pwhash import str
from tornado.escape import json_decode, utf8
from tornado.gen import coroutine

from .base import BaseHandler

class RegistrationHandler(BaseHandler):

    @coroutine
    def post(self):
        if self.request.body:
            body = json_decode(self.request.body)
            username = body['username']
            password = body['password']
        else:
            self.send_error(400, message='You must provide a username and password!')
            return

        user = yield self.db.users.find_one({'username': username})

        if user is not None:
            self.send_error(400, message='User already exists!')
            return

        password_hash = yield self.executor.submit(str, utf8(password))

        yield self.db.users.insert_one({
            'username': username,
            'password_hash': password_hash
        })

        self.set_status(200)
        self.response['username'] = username
        self.write_json()
