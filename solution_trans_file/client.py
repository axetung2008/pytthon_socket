import socket
import threading
import os

import buffer

HOST = '168.138.53.103'
PORT = 8888

s = socket.socket()
s.connect((HOST, PORT))

with s:
    sbuf = buffer.Buffer(s)

    # hash_type = input('Enter hash type: ')

    files = input('Enter file(s) to send: ')
    files_to_send = files.split()

    for file_name in files_to_send:
        print(file_name)
        # sbuf.put_utf8(hash_type)
        sbuf.put_utf8(file_name)

        file_size = os.path.getsize(file_name)
        sbuf.put_utf8(str(file_size))

        with open(file_name, 'rb') as f:
            sbuf.put_bytes(f.read())
        print('File Sent')