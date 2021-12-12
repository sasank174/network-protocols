import socket

s = socket.socket()
host = socket.gethostbyname(socket.gethostname())
port = 1234

text_file = open("mytext.txt", "w")

se1=input("enter items purchased by customer 1 ")
se2=input("enter items purchased by customer 2 ")
text_file.write(se1)
text_file.write("\n")
text_file.write(se2)
text_file.close()

s.connect((host,port))
s.send(b"hello server!")

with open("received_file.txt","wb") as f:
	print("file opened")
	print("rceiving data")
	data = s.recv(1024)
	print("data= ",data)
	f.write(data)
f.close()