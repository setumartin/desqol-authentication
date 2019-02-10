from tornado.gen import coroutine
from tornado.web import authenticated

from .auth import AuthHandler

class LogoutHandler(AuthHandler):

    @coroutine
    @authenticated
    def post(self):
        yield self.db.users.update_one({
            'username': self.current_user['username'],
        }, {
            '$set': {
                'token': None
            }
        })
        
        self.current_user = None

        self.set_status(200)
        self.write_json()
