import socket
import sys

# Create a TCP/IP socket
ecs = socket.socket(2,1,0)
# Connect the socket to the port where the server is listening
server_address = ('127.0.0.1', 50000)
#server_address = ('67.214.219.123', 50000)
ecs.connect(server_address)


try:
    # Send data
    message = "5|6"
    ecs.sendall(message)
    # print the response
    print ecs.recv(64)

finally:
    # close the socket to clean up
	ecs.close()