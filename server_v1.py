import socket
import sys
import subprocess
import os
import tqdm

BUFFER_SIZE_FILE = 4096 # send 4096 bytes each time step

# Create a Socket ( connect two computers)
def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 8888
        s = socket.socket()

    except socket.error as msg:
        print("Socket creation error: " + str(msg))


# Binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding the Port: " + str(port))

        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print("Socket Binding error" + str(msg) + "\n" + "Retrying...")
        bind_socket()


# Establish connection with a client (socket must be listening)

def socket_accept():
    conn, address = s.accept()
    print("Connection has been established! |" + " IP " + address[0] + " | Port" + str(address[1]))
    #recv_commands(conn)
    recv_commands(conn)
    conn.close()
# def recv_file(conn):
#     BUFFER_SIZE = 4096
#     SEPARATOR = "<SEPARATOR>"
#     received = conn.recv(BUFFER_SIZE).decode()
#     filename, filesize = received.split(SEPARATOR)
#     # remove absolute path if there is
#     filename = os.path.basename(filename)
#     # convert to integer
#     filesize = int(filesize)
#     with open(filename, "wb") as f:
#         while True:
#         # read 1024 bytes from the socket (receive)
#             bytes_read = conn.recv(BUFFER_SIZE)
#             if not bytes_read:    
#             # nothing is received
#             # file transmitting is done
#                 break
#         # write to the file the bytes we just received
#             f.write(bytes_read)
#     pass
#Debug
def recv_commands(conn):
    while True:
        #Xu ly du lieu tu client gui len
        msg = conn.recv(1024)
        from_client = msg.decode("utf-8")
        if from_client == "disconnect":
            conn.send(bytes("Disconnected!","utf-8"))
            break
        command = from_client.split()
       
        #Xu ly cd
        if command[0] == "cd":
            cd(conn,command)
            continue
        #Xu lu cac command khac
        all_command(conn,command)


def cd(conn,command):
    os.chdir(command[1])
    path = os.getcwd()
    conn.send(bytes(path,"utf-8"))
def all_command(conn,command):
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
        if command[0] == "mkdir":
            conn.send(bytes("Folder created!","utf-8"))
        if command[0] == "rm":
            conn.send(bytes("File or folder deleted","utf-8"))
        
        conn.send(bytes(output.decode(),"utf-8"))
    except FileNotFoundError as e:
        conn.send(bytes("Command not found. Please try again!","utf-8"))

def main():
    create_socket()
    bind_socket()
    socket_accept()


main()