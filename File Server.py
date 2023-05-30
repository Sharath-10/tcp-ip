import socket
import sys
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address=('localhost',10900)
server.bind(server_address)
server.listen(1)
connection, client_address=server.accept()
file_name="Msg.txt"
connection.sendall(file_name.encode())
file=open("Msg.txt","rb")
data=file.read()
connection.sendall(data)
file.close()
connection.close()
server.close()