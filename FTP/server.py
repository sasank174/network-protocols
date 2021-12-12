import socket

def common_member(a, b):
	a_set = set(a)
	b_set = set(b)
	if (a_set & b_set):
		return len(a_set & b_set)
	else:
		print("No common elements")

s = socket.socket()
host = socket.gethostbyname(socket.gethostname())
port = 1234
s.bind((host,port))
s.listen(5)

print("server is listning")

while True:
	conn, addr = s.accept()
	print("got connection from ",addr)
	data = conn.recv(1024)
	print("server received ",repr(data))

	x = []
	filename = "mytext.txt"
	f = open(filename,"rb")
	l = f.readline()
	inp = str(l, 'utf-8')
	inp1 = inp.split(" ")
	l = f.readline()
	inp = str(l, 'utf-8')
	inp2 = inp.split(" ")
	print(inp1)
	print(inp2)
	ans = common_member(inp1,inp2)
	ans = str(ans).encode()
	conn.send(ans)
	
	f.close()