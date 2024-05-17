def upload_file(conn, file):
    with open(file, 'rb') as f:
        while True:
            chunk = f.read(1024)
            if not chunk:
                break
            conn.sendall(chunk)
    f.close()


def download_file(conn, file):
    with open(file, 'wb') as f:
        while True:
            chunk = conn.recv(1024)
            if not chunk:
                break
            f.write(chunk)
