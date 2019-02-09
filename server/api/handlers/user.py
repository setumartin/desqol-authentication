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
        self.response['displayName'] = self.current_user['display_name']
        self.write_json()

    @tornado.gen.coroutine
    @tornado.web.authenticated
    def put(self):
        try:
            if self.request.body:
                body = tornado.escape.json_decode(self.request.body)
                display_name = body['displayName']
            else:
                raise Exception()
        except:
            self.send_error(400, message='You must provide a displayName!')
            return

        yield self.db.users.update_one({
            'username': self.current_user['username'],
        }, {
            '$set': {
                'displayName': display_name
            }
        })
        
        self.current_user['display_name'] = display_name

        self.set_status(200)
        self.response['username'] = self.current_user['username']
        self.response['displayName'] = self.current_user['display_name']
        self.write_json()
