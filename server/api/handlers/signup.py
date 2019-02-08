import json
import nacl.pwhash
import tornado.escape
import tornado.gen

from .base import BaseHandler

class SignupHandler(BaseHandler):

    @tornado.gen.coroutine
    def post(self):
        if self.request.body:
          body = tornado.escape.json_decode(self.request.body)
          username = body['username']
          password = body['password']
        else:
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
