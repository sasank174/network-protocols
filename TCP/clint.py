import socket
import socket 
n = input("enter whom to vote ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('sasank', 9999))
client.send(str.encode(n))
response = client.recv(4096)
print("=========election results=========")
x = response.decode('utf8').strip('\n')
x = x.split("---")
x = [int(v) for v in x]
maxval = max(x[:-1])
indexval = x.index(maxval)+1
print("MESSAGE FROM server is '" + str(indexval) + "' has won elections")
print("There are " +str(x[-1]) + " spoilt ballots")