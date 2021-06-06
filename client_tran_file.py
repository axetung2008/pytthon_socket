import socket
import os
import subprocess
import tqdm

s = socket.socket()
host = '168.138.53.103'
port = 8888
SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 # send 4096 bytes each time step
s.connect((host, port))



while True:
    filename = input()

    # filesize = os.path.getsize(filename)

    s.send(bytes(filename,"utf-8"))

    # txt = s.recv(BUFFER_SIZE).decode()
    # print(filename)

    with open(filename, "rb") as f:
        while True:
            # read the bytes from the file
            bytes_read = f.read(BUFFER_SIZE)
            # print(bytes_read)
            # a = str(bytes_read)
            # print(type(a))
            # print(a == "b''")
            # print(bytes_read.decode())
            if not bytes_read:
                # file transmitting is done
                # print("not bytes_read")
                s.sendall(bytes_read)
                break
            # we use sendall to assure transimission in 
            # busy networks
            # if a == "b''":
            #     print("true")
            #     break
            s.sendall(bytes_read)
            # print("SEND!")

            # s.send(bytes(bytes_read),"utf-8")
            # update the progress bar
            # progress.update(len(bytes_read))
#============================================

    


s.close()