import socket 
n = int(input("enter whom to vote "))

msgFromClient = str(n)
bytesToSend  = str.encode(msgFromClient)
serverAddressPort = ("sasank",20001)
bufferSize  = 1080
UDPClientSocket = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
UDPClientSocket.sendto(bytesToSend, serverAddressPort)
msgFromServer = UDPClientSocket.recvfrom(bufferSize)
print("=========election results=========")
x = msgFromServer[0].decode('utf8').strip('\n')
x = x.split("---")
x = [int(v) for v in x]
maxval = max(x[:-1])
indexval = x.index(maxval)+1
print("MESSAGE FROM server is '" + str(indexval) + "' has won elections")
print("There are " +str(x[-1]) + " spoilt ballots")