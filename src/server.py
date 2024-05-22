import socket
import os

host = '127.0.0.1'
port = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)
print('listening on', port)

client, addr = server.accept()
print('connected to', addr)

while True:
    comm = input(f'{addr}% ')
    if comm == 'close':
        client.send(comm.encode())
        break
    elif comm[:3] == 'cd ':
        client.send(comm.encode())
    elif comm == 'clean':
        os.system(comm)
    elif comm.strip() == '':
        pass
    else:
        client.send(comm.encode())
        output = client.recv(1024).decode()
        print(output)

server.close()
