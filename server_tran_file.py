import socket
import sys
import subprocess
import os
import tqdm

BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"
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
    # recv_commands(conn)
    recv_file(conn)
    conn.close()

def recv_file(conn):
    while True:
        
        # filename = conn.recv(BUFFER_SIZE).decode("utf-8")
        from_client = conn.recv(BUFFER_SIZE)
        path = from_client.decode("utf-8")
        print(path)
        if path == "":
            print("Co chuoi rong!")
            break
        # remove absolute path if there is
        filename = os.path.basename(path)
        # print("os.path.basename:",filename)

        conn.send(bytes("Da nhan file!","utf-8"))
        # convert to integer
        getFile(conn, filename)
        # with open(filename, "wb") as f:
        #     while True:
        #         bytes_read = conn.recv(BUFFER_SIZE)
        #         if not bytes_read:    
        #             # nothing is received
        #             # file transmitting is done
        #             print("transmitting is done")
        #             break
                
        #         f.write(bytes_read)
def getFile(conn, filename):
        
    with open(filename, "wb") as f:
        while True:
            bytes_read = conn.recv(BUFFER_SIZE)
            print(bytes_read)
            if not bytes_read:    
                # nothing is received
                # file transmitting is done
                print("transmitting is done")
                break
            
            f.write(bytes_read)
            print("in while")
            # break

def main():
    create_socket()
    bind_socket()
    socket_accept()


main()