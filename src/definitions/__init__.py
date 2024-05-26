import string
from random import shuffle


def send_error(conn, msg):
    error_msg = f'[From client] {msg}'
    conn.send(error_msg.encode())


def random_filename():
    letters = string.ascii_letters
    number = string.digits
    characters = list(letters + number)
    shuffle(characters)
    filename = ''.join(characters[:5])
    return filename


def upload(conn, file):
    f = open(file, 'rb')
    conn.send(f.read())


def download(conn, file):
    f = open(file, 'wb+')
    client.settimeout(5)
    chunk = conn.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            chunk = conn.recv(1024)
        except socket.timeout as e:
            break
    conn.settimeout(None)
    f.close()


def screnshot_client():
    shot = ImageGrab.grab()
    shot.save(f'screenshot.png')
    shot.close()


def screenshot_server(conn):
    filename = random_filename()
    file = f'shot-{filename}.png'
    f = open(file, 'wb+')
    conn.settimeout(5)
    chunk = conn.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            chunk = conn.recv(1024)
        except socket.timeout as e:
            break
    conn.settiemout(None)
    f.close()

