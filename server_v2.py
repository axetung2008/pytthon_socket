import socket
import sys
import subprocess
import os


BUFFER_SIZE_FILE = 4096 # send 4096 bytes each time step

# Create a Socket ( connect two computers)
def create_socket():
    try:
        global host
        global port
        global s

        #=======socket for upload file========
        global port_file
        global s_file
        port_file = 8989
        s_file = socket.socket()
        #=====================================

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
        #======bind for upload file==========
        global port_file
        global s_file
        #====================================
        print("Binding the Port(s): " + str(port))
        print("Binding the Port(s): " + str(port_file))

        

        s.bind((host, port))
        s.listen(5)

        #========file==========
        s_file.bind((host,port_file))
        s_file.listen(10)


    except socket.error as msg:
        print("Socket Binding error" + str(msg) + "\n" + "Retrying...")
        bind_socket()


# Establish connection with a client (socket must be listening)

def socket_accept():
    conn, address = s.accept()
    conn_file, address_file = s.accept()
    print("Connection has been established! |" + " IP " + address[0] + " | Port" + str(address[1]))
    recv_commands(conn)
    conn.close()
# def recv_file(conn):
#     import buffer

#     HOST = ''
#     PORT = 8989

#     # If server and client run in same local directory,
#     # need a separate place to store the uploads.
#     try:
#         os.mkdir('uploads')
#     except FileExistsError:
#         pass

#     s = socket.socket()
#     s.bind((HOST, PORT))
#     s.listen(10)
#     print("Waiting for a connection.....")

#     while True:
#         conn, addr = s.accept()
#         print("Got a connection from ", addr)
#         connbuf = buffer.Buffer(conn)

#         while True:
            
#             file_name = connbuf.get_utf8()
#             if not file_name:
#                 break
#             file_name = os.path.basename(file_name)
#             file_name = os.path.join('uploads',file_name)
#             print('file name: ', file_name)

#             file_size = int(connbuf.get_utf8())
#             print('file size: ', file_size )

#             with open(file_name, 'wb') as f:
#                 remaining = file_size
#                 while remaining:
#                     chunk_size = 4096 if remaining >= 4096 else remaining
#                     chunk = connbuf.get_bytes(chunk_size)
#                     print(chunk)
#                     if not chunk: break
#                     f.write(chunk)
#                     remaining -= len(chunk)
#                 if remaining:
#                     print('File incomplete.  Missing',remaining,'bytes.')
#                 else:
#                     print('File received successfully.')
#         print('Connection closed.')
#         conn.close()

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