""" 
The client for serverecho.py
""" 

import socket 
import time

host = 'derekbot.servegame.com' 
port = 25565 
size = 1024 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

s.connect((host,port)) 
print "connected"
s.send('user')
time.sleep(2)

while True:
    time.sleep(2)
    s.send('Ahoy')
