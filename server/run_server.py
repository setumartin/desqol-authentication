from logging import basicConfig, INFO, info
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

from api.conf import HOST, PORT
from api.app import Application

def main():
    basicConfig(level=INFO)

    http_server = HTTPServer(Application())
    http_server.listen(PORT, HOST)

    info('Starting server...')
    IOLoop.current().start()

if __name__ == '__main__':
    main()
