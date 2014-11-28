""" 
A server which echos any messages sent to it.
""" 

import socket
host = '' 
port = 25565 
backlog = 5 
size = 1024 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind((host,port)) 
s.listen(backlog)
 
print "Listening"
while 1: 
	client, address = s.accept() 
	print "Found client"
	
	data = client.recv(size) 
	
	if data:
		print "Revived data: " + str(data)
		client.send(data) 
		
	client.close()
	print "Client closed"