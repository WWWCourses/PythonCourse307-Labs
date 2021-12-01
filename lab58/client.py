import socket
import threading

PORT = 5050
SERVER_IP = '192.168.100.38'
# SERVER_IP = '127.0.0.1'
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'end'
BUFF_SIZE=4096

def connect_to_server():
	# create an INET (i.e. IPv4), STREAMing (i.e. TCP) socket:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# reuse address (optional, only for test purposes)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	# bind the socket to the host
	s.connect((SERVER_IP, PORT))

	return s

def receive_message(s):
	while True:
		try:
			msg_bytes = s.recv(BUFF_SIZE)
			msg = msg_bytes.decode(FORMAT)
			if msg == "":
				print("Server is down!")
				exit(0)
			print(f'\n\t{msg}')
		except Exception as e:
			print(f'Error: {e}')
			s.close()
			break


def send_message(s,msg):
	message = msg.encode(FORMAT)
	msg_length = len(message)
	send_length = str(msg_length).encode(FORMAT)

	# pad message to be send to BUFF_SIZE
	send_length += b' ' * (BUFF_SIZE - len(send_length))

	s.send(send_length)
	s.send(message)

	# print(s.recv(BUFF_SIZE).decode(FORMAT))


if __name__ == '__main__':
	s = connect_to_server()

	# start thread for receiving messages
	tr = threading.Thread(target=receive_message, args=(s,),daemon=True)
	tr.start()

	while True:
		msg = input("Enter a message:")
		if msg == '':
			send_message(s,DISCONNECT_MESSAGE)
		else:
			send_message(s,msg)

