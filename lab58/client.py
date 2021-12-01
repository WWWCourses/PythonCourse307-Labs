import socket

PORT = 5050
SERVER_IP = '192.168.100.38'
# SERVER_IP = '127.0.0.1'
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'end'
BUFF_SIZE=4096

# create an INET (i.e. IPv4), STREAMing (i.e. TCP) socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# reuse address (optional, only for test purposes)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# bind the socket to the host
s.connect((SERVER_IP, PORT))


def send(msg):
	message = msg.encode(FORMAT)
	msg_length = len(message)
	send_length = str(msg_length).encode(FORMAT)

	# pad message to be send to BUFF_SIZE
	send_length += b' ' * (BUFF_SIZE - len(send_length))

	s.send(send_length)
	s.send(message)

	print(s.recv(BUFF_SIZE).decode(FORMAT))

while True:
	msg = input("Enter a message:")
	if msg == '':
		send(DISCONNECT_MESSAGE)
	else:
		send(msg)