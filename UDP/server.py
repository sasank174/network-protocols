import socket
import time

localIP = "sasank"
localPort = 20001
bufferSize = 1080
msgFromServer = "10"


remember = [0,0,0,0,0,0]

def election(x):
	x = x.decode('utf8').strip('\n')
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

UDPServerSocket = socket.socket(family=socket.AF_INET,type = socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP,localPort))
print("UDP server up and listening")
while(True):
	bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
	message = bytesAddressPair[0]
	address = bytesAddressPair[1]
	clientMsg = "Message from client:{}".format(message)
	election(message)

	print(clientMsg)
	time.sleep(1)

	UDPServerSocket.sendto(str.encode(msgFromServer), address)