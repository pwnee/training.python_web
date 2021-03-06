#!/usr/bin/env python

import socket 
import email

#"Wed, 09 Feb 1994 22:23:32 GMT" 
def get_date():
	date = str(email.Utils.formatdate())
	return date


def ok_response(body):	
	date = get_date()	
	return_data = "HTTP/1.0 200 OK\r\n Content-Type: text/html\r\nDate: {0}\r\n\r\n{1}".format(date,body) 
	return (return_data)

host = '' # listen on all connections (WiFi, etc) 
port = 50000 
backlog = 5 # how many connections can we stack up
size = 1024 # number of bytes to receive at once

http_data = "<html>\n<body>\n<h1>This is a header</h1>\n<p>and this is some regular text</p>\n<p>\nand some more\n</p>\n</body>\n</html>"

## create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# set an option to tell the OS to re-use the socket
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# the bind makes it a server
s.bind( (host,port) ) 
s.listen(backlog) 

while True: # keep looking for new connections forever
    client, address = s.accept() # look for a connection
    data = client.recv(size)
    if data: # if the connection was closed there would be no data
        print "received: %s, sending it back"%data
        client.send(ok_response(http_data)) 
        client.close()