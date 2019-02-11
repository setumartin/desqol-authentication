from datetime import datetime, timedelta
from nacl.hash import blake2b
from nacl.pwhash import verify
from time import mktime
from tornado.escape import json_decode, utf8
from tornado.gen import coroutine
from uuid import uuid4

from .base import BaseHandler

class LoginHandler(BaseHandler):

    @coroutine
    def generate_token(self, username):
        token_uuid = uuid4().hex
        token_hash = blake2b(token_uuid.encode(), key=self.hmac_key)
        expires_in = datetime.now() + timedelta(hours=2)
        expires_in = mktime(expires_in.utctimetuple())

        token = {
            'token': token_hash.decode('utf-8'),
            'expiresIn': expires_in,
        }

        yield self.db.users.update_one({
          'username': username
        }, {
          '$set': token
        })

        return token

    @coroutine
    def post(self):
        try:
            if self.request.body:
                body = json_decode(self.request.body)
                username = body['username']
                password = body['password']
            else:
                raise Exception()
        except:
            self.send_error(400, message='You must provide a username and password!')
            return

        if not username:
            self.send_error(400, message='The username is invalid!')
            return

        if not password:
            self.send_error(400, message='The password is invalid!')
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
        except nacl.exceptions.InvalidkeyError:
            self.send_error(403, message='The username and password are invalid!')
            return

        token = yield self.generate_token(username)

        self.set_status(200)
        self.response['token'] = token['token']
        self.response['expiresIn'] = token['expiresIn']
        self.write_json()
