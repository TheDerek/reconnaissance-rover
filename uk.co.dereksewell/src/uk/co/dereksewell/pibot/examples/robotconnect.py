""" 
The client for serverecho.py
""" 

import socket 
import time

def move(string):
    pass

host = 'derekbot.servegame.com' 
port = 25565 
size = 1024 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

s.connect((host,port)) 
print "connected"
s.send('robot')
time.sleep(2)

while True:
    data = s.recv(size)
    if data:
        print "Received: \"" + data + "\" from user"
        move(data)
