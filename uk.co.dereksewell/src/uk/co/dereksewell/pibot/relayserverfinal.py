""" 
A server which echos any messages sent to it.
"""

import socket
import thread
import time
import tornado.websocket
import tornado.ioloop
import tornado.httpserver
import tornado.web
import sys

command = "0"
command2 = command
commandMatchTime = 0

host = ''
port = 25565
backlog = 5
size = 5024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(backlog)

#Address = ws://86.163.159.40:8888/ws

class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print 'New client connection was opened'
        self.write_message("Welcome to my websocket!")

    def on_message(self, message):
        print 'Incoming message:', message
        command = message
        client.send(message)

    def on_close(self):
        print 'Connection was closed...'

def listenOnClient(client):
    """Listens for incomming data from the
    client and overrides the command variable
    once data has been recived."""
    while True:
        data = client.recv(size)
        if data:
            print "Received: \"" + data + "\" from user"
            command = data


def relayOnClient(client):
    """Sends the last received command to the robot, effectively relaying the command."""
    while True:

        time.sleep(0.1)
        #Constantly sends the last received command to the client


application = tornado.web.Application([(r'/ws', WSHandler)])
http_server = tornado.httpserver.HTTPServer(application)
http_server.listen(8888)
http_server.start()
t = thread.start_new_thread(tornado.ioloop.IOLoop.instance().start, ())

while True:

    try:
        print "Listening"
        #Constantly listens for new clientswhile 1:
        client, address = s.accept()
        print "Found client at: " + str(address)

        print "new robot connected"
        #Starts a new thread for sending to the robot
        #thread.start_new_thread(relayOnClient(client), ())



    except socket.error, (value, message):
        if s:
            s.close()
        print "Connection Failed: " + message
