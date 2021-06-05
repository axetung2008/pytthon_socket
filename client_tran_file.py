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
# while True:
    
filename = input()
# filename = "D:/ca_lia_thia_1.png"
filesize = os.path.getsize(filename)

s.send(f"{filename}{SEPARATOR}{filesize}".encode())
# s.send(filename.decode())
# progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "rb") as f:
    while True:
        # read the bytes from the file
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            # file transmitting is done
            break
        # we use sendall to assure transimission in 
        # busy networks
        s.sendall(bytes_read)
        # update the progress bar
        # progress.update(len(bytes_read))
# close the socket

s.close()