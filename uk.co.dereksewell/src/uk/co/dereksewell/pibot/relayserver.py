""" 
A server which echos any messages sent to it.
"""

import socket
import thread
import time
import sys


command = "0"
host = ''
port = 25565
backlog = 5
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(backlog)


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
        client.send(command)


print "Listening"

#Constantly listens for new clientswhile 1:
client, address = s.accept()
print "Found client at: " + str(address)
data = client.recv(size)

while True:
    if data == "user":
        while True:
            print "new user connected"
            #Starts a new thread for listening to the client
            thread.start_new_thread(listenOnClient(client), ())

    if data == "robot":
        print "new robot connected"
        #Starts a new thread for sending to the robot
        thread.start_new_thread(relayOnClient(client), ())

