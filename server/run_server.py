import tornado.httpserver
import tornado.ioloop
import webapp.conf
import webapp.app

def main():

    http_server = tornado.httpserver.HTTPServer(webapp.app.Application())
    http_server.listen(webapp.conf.PORT, webapp.conf.HOST)

    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()
