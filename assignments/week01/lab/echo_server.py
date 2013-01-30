import socket
import sys

# Create a TCP/IP socket
ess = socket.socket(2,1,0)
# Bind the socket to the port
#server_address = ('127.0.0.1', 50000)
ess.bind(('127.0.0.1', 50000))
# Listen for incoming connections
ess.listen(1)
while True:
    # Wait for a connection
	con, cli = ess.accept()
	try:
        # Receive the data and send it back
			echo = con.recv(64)
			
			con.sendall(echo)

	finally:
			# Clean up the connection
			con.close()
