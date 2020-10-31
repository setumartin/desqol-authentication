from datetime import datetime, timedelta
from nacl.exceptions import InvalidkeyError
from nacl.hash import blake2b
from nacl.pwhash import verify
from time import mktime
from tornado.escape import json_decode, utf8
from tornado.gen import coroutine
from uuid import uuid4

from .base import BaseHandler

class LoginHandler(BaseHandler):

    @coroutine
    def generate_token(self, email):
        token_uuid = uuid4().hex
        token_hash = blake2b(token_uuid.encode(), key=self.hmac_key)
        expires_in = datetime.now() + timedelta(hours=2)
        expires_in = mktime(expires_in.utctimetuple())

        token = {
            'token': token_hash.decode('utf-8'),
            'expiresIn': expires_in,
        }

        yield self.db.users.update_one({
            'email': email
        }, {
            '$set': token
        })

        return token

    @coroutine
    def post(self):
        try:
            body = json_decode(self.request.body)
            email = body['email']
            if not isinstance(email, str):
                raise Exception()
            password = body['password']
            if not isinstance(password, str):
                raise Exception()
        except:
            self.send_error(400, message='You must provide an email address and password!')
            return

        if not email:
            self.send_error(400, message='The email address is invalid!')
            return

        if not password:
            self.send_error(400, message='The password is invalid!')
            return

        user = yield self.db.users.find_one({'email': email})

        if user is None:
            self.send_error(403, message='The email address and password are invalid!')
            return

        try:
            yield self.executor.submit(
                verify,
                user['passwordHash'],
                utf8(password)
            )
        except InvalidkeyError:
            self.send_error(403, message='The email address and password are invalid!')
            return

        token = yield self.generate_token(email)

        self.set_status(200)
        self.response['token'] = token['token']
        self.response['expiresIn'] = token['expiresIn']
        self.response['gamify'] = user.get('gamify')
        self.write_json()
