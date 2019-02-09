import json
import nacl.pwhash
import tornado.escape
import tornado.gen

from .base import BaseHandler

class RegistrationHandler(BaseHandler):

    @tornado.gen.coroutine
    def post(self):
        try:
          if self.request.body:
              body = tornado.escape.json_decode(self.request.body)
              username = body['username']
              password = body['password']
              display_name = body['displayName']
          else:
            raise Exception()
        except Exception:
            self.send_error(400, message='You must provide a username, password and displayName!')
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
            'passwordHash': password_hash,
            'displayName': display_name
        })

        self.set_status(200)
        self.response['username'] = username
        self.response['displayName'] = display_name
        self.write_json()
