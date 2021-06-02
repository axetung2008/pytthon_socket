import socket
import os
import subprocess

s = socket.socket()
host = '168.138.53.103'
port = 8888

s.connect((host, port))
while True:
    a = input()
    s.send(bytes(a, "utf-8"))
    if a == "exit":
        print("Ket thuc")
        break
    from_server = s.recv(2048)
    # result_from_server = from_server.decode("utf-8")
    print(from_server.decode())
s.close()

