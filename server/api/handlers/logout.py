import tornado.escape
import tornado.gen
import tornado.web

from .auth import AuthHandler

class LogoutHandler(AuthHandler):

    @tornado.gen.coroutine
    @tornado.web.authenticated
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
