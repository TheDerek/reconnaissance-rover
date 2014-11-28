""" 
The client for serverecho.py
""" 

import socket 

host = 'derekbot.servegame.com' 
port = 25565 
size = 1024 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

s.connect((host,port)) 
print "connected"
s.send('Hello, world') 
data = s.recv(size) 
s.close() 

print 'Received:', data