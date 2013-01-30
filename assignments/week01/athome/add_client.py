import socket
import sys
from number_checker import *

# Create a TCP/IP socket
ecs = socket.socket(socket.AF_INET,
					socket.SOCK_STREAM,
					socket.IPPROTO_IP)
# Connect the socket to the port where the server is listening
# IP Address could change, set it below
uw_ip = '67.214.219.123'
remote_address = (uw_ip, 50000)
ecs.connect(remote_address)

#Get the numbers to add from the user
number1 = get_number()
number2 = get_number()
#Put the numbers into a string to send via socket
# TODO: Think about pickling data instead of going to strings.
data = str(number1) + "|" + str(number2)

try:
    #Send data
    print "Sending the numbers to web server..."
    ecs.sendall(data)
	# Print the response
    print "The web server returned:", ecs.recv(64)  
  
finally:
    # close the socket to clean up
    ecs.close()