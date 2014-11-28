import tornado.websocket
import tornado.ioloop
import tornado.httpserver
import tornado.web


class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print 'New connection was opened'
        self.write_message("Welcome to my websocket!")

    def on_message(self, message):
        print 'Incoming message:', message
        self.write_message("You said: " + message)

    def on_close(self):
        print 'Connection was closed...'

application = tornado.web.Application([(r"/ws", WSHandler)])
http_server = tornado.httpserver.HTTPServer(application)
http_server.listen(25565)
http_server.start()
tornado.ioloop.IOLoop.instance().start()