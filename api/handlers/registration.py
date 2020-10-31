from json import dumps
from nacl.pwhash import str as nacl_str
from tornado.escape import json_decode, utf8
from tornado.gen import coroutine

from .base import BaseHandler

class RegistrationHandler(BaseHandler):

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
            display_name = body['displayName']
            if not isinstance(display_name, str):
                raise Exception()
        except Exception as e:
            self.send_error(400, message='You must provide an email address, password and display name!')
            return

        if not email:
            self.send_error(400, message='The email address is invalid!')
            return

        if not password:
            self.send_error(400, message='The password is invalid!')
            return

        if not display_name:
            self.send_error(400, message='The display name is invalid!')
            return

        user = yield self.db.users.find_one({'email': email})

        if user is not None:
            self.send_error(409, message='A user with the given email address already exists!')
            return

        gamify = None

        if self.whitelist:
            user_2 = yield self.db.whitelist.find_one({'email': email})
            if user_2:
                gamify = user_2['gamify']
            else:
                self.send_error(403, message='The email address is not on the whitelist!')
                return

        password_hash = yield self.executor.submit(nacl_str, utf8(password))

        yield self.db.users.insert_one({
            'email': email,
            'passwordHash': password_hash,
            'displayName': display_name,
            'gamify': gamify,
        })

        self.set_status(200)
        self.response['email'] = email
        self.response['displayName'] = display_name
        self.response['gamify'] = gamify
        self.write_json()
