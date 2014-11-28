import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import tornado
import serial
from threading import Thread
import thread
import time
from multiprocessing import Process
 
class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print 'new connection'
        self.write_message("Hello World")
      
    def on_message(self, message):
        act(message)
        print 'message received %s' % message
 
    def on_close(self):
        print 'connection closed'
 
 
application = tornado.web.Application([(r'/', WSHandler)])

def act(message):
    #Key:
    #xyzzz
    #x = motor, 1 or 2
    #y = type:
        #f = forwards
        #b = backwards
        #r = Release
        
        #zzz = power from 0-255
        
    time.sleep(0.05);
    ser.write(message)
    print "Wrote message: " + message
    
#def reciveInput():
#    while True:
        #print "Awaiting on orders Captin"
 #       if ser.inWaiting() > 0:
 #           print ser.readline()
        
 #       act("f 1 255")
 
if __name__ == "__main__":
    ser = serial.Serial('COM6', 115200)
    ser.setDTR(False)	
    #Thread(target=reciveInput(), args=()).start()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(25565)
    http_server.start();
    tornado.ioloop.IOLoop.instance().start()
    
    
    
    
