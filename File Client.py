import socket
import sys
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address=('localhost',10900)
client.connect(server_address)
file_name=client.recv(1000).decode()
file_name="hello"+file_name
file=open(file_name,"wb")
data=client.recv(4097)
file.write(data)
file.close()
client.close()