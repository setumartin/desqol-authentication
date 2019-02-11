from nacl.pwhash import str
from tornado.escape import json_decode, utf8
from tornado.gen import coroutine
from tornado.web import authenticated

from .auth import AuthHandler

class UserHandler(AuthHandler):

    @authenticated
    def get(self):
        self.set_status(200)
        self.response['email'] = self.current_user['email']
        self.response['displayName'] = self.current_user['display_name']
        self.write_json()

    @coroutine
    @authenticated
    def put(self):
        try:
            if self.request.body:
                body = json_decode(self.request.body)
                display_name = body['displayName']
            else:
                raise Exception()
        except:
            self.send_error(400, message='You must provide a displayName!')
            return

        if not display_name:
            self.send_error(400, message='The displayName is invalid!')
            return

        yield self.db.users.update_one({
            'email': self.current_user['email'],
        }, {
            '$set': {
                'displayName': display_name
            }
        })
        
        self.current_user['display_name'] = display_name

        self.set_status(200)
        self.response['email'] = self.current_user['email']
        self.response['displayName'] = self.current_user['display_name']
        self.write_json()
