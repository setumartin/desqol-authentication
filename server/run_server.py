import logging
import tornado.httpserver
import tornado.ioloop
import api.conf
import api.app

def main():
    logging.basicConfig(level=logging.INFO)

    http_server = tornado.httpserver.HTTPServer(api.app.Application())
    http_server.listen(api.conf.PORT, api.conf.HOST)

    logging.info('Starting server...')
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()
