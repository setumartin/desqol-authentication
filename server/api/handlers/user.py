import nacl.pwhash
import tornado.escape
import tornado.gen
import tornado.web

from .auth import AuthHandler

class UserHandler(AuthHandler):

    @tornado.web.authenticated
    def get(self):
        self.set_status(200)
        self.response['username'] = self.current_user['username']
        self.write_json()

    @tornado.gen.coroutine
    @tornado.web.authenticated
    def put(self):
        if self.request.body:
            body = tornado.escape.json_decode(self.request.body)
            password = body['password']
        else:
            self.send_error(400, message='You must provide a password!')
            return

        if password is not None:
            password_hash = yield self.executor.submit(
                nacl.pwhash.str,
                tornado.escape.utf8(password)
            )

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
