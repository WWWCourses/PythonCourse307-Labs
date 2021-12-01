import socket
import threading

PORT = 5050
SERVER_IP = socket.gethostbyname(socket.gethostname())
# SERVER_IP = '127.0.0.1'
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'end'
BUFF_SIZE=4096


# create an INET (i.e. IPv4), STREAMing (i.e. TCP) socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# reuse address (optional, only for test purposes)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# bind the socket to the host
s.bind((SERVER_IP, PORT))

s.listen()
print(f"Server is listening on {SERVER_IP}:{PORT}")

clients = []

def handle_client(conn, addr):
	print(f"[NEW CONNECTION] {addr} connected.")
	connected = True

	while connected:
		msg_length = conn.recv(BUFF_SIZE)

		if msg_length:
			msg_length = int(msg_length)
			msg = conn.recv(msg_length).decode(FORMAT)

			if msg == DISCONNECT_MESSAGE:
				connected = False

			print(f'Msg received: {msg}')
			print(f"[{addr}] {msg}")

			# TASK: send message to all other clients, except current

			# conn.send("Msg received".encode(FORMAT))

	conn.close()

while True:
	conn, addr = s.accept()

	# TASK: add conn to clients list

	print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

	tr = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
	tr.start()




