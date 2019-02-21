from .base import BaseHandler

class WelcomeHandler(BaseHandler):

    def get(self):
        self.write('Welcome to the Erasmus+ DESQOL Authentication Server!')
