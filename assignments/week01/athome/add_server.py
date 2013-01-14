import socket
import sys
import exceptions

# Function from StackOverflow to deal with floats
def num (s):
    try:
        return int(s)
    except exceptions.ValueError:
        return float(s)	


# Create a TCP/IP socket
ess = socket.socket(2,1,0)
# Bind the socket to the port
#server_address = ('127.0.0.1', 50000)
ess.bind(('67.214.219.123', 50000))
# Listen for incoming connections
ess.listen(1)
while True:
    # Wait for a connection
	con, cli = ess.accept()
	try:
        # Receive the data and send it back
		echo = con.recv(64)
		num1,num2 = echo.split("|",1)
		sum_of_numbers = num(num1) + num(num2)
		sum_of_numbers = str(sum_of_numbers)
		con.sendall(sum_of_numbers)

	finally:
		# Clean up the connection
		con.close()
