from gitinfo import get_git_info

from .base import BaseHandler

class WelcomeHandler(BaseHandler):

    def get(self):
        git_info = get_git_info()
      
        self.set_status(200)
        self.response['message'] = 'Welcome to the Erasmus+ DESQOL Authentication Server!';
        if git_info:
            self.response['commit'] = git_info['commit'];
        self.write_json()
