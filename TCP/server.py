import socket
import threading

bind_ip = 'sasank'
bind_port = 9999
max_connections = 5

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(max_connections)

print (('Listening on {}:{}').format(bind_ip, bind_port))

msgFromServer = "10"


remember = [0,0,0,0,0,0]

def election(x):
	# x = x.decode('utf8').strip('\n')
	x= int(x)
	global msgFromServer
	if x == 1:
		remember[0] = remember[0]+1
	elif x == 2:
		remember[1] = remember[1]+1
	elif x == 3:
		remember[2] = remember[2]+1
	elif x == 4:
		remember[3] = remember[3]+1
	elif x == 5:
		remember[4] = remember[4]+1
	else:
		remember[5] = remember[5]+1
	msgFromServer = "---".join(str(v) for v in remember)
	return msgFromServer

def handle_client_connection(client_socket):
    request = client_socket.recv(4096 )
    print (int(request))
    ans = election(int(request))
    client_socket.send(str.encode(ans))
    client_socket.close()

while True:
    client_sock, address = server.accept()
    print (('Accepted connection from {}:{}').format(address[0], address[1]))
    client_handler = threading.Thread(
        target=handle_client_connection,
        args=(client_sock,))
    client_handler.start()