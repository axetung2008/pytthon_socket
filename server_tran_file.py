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
	received = conn.recv(BUFFER_SIZE).decode()
	filename, filesize = received.split(SEPARATOR)
	# remove absolute path if there is
	filename = os.path.basename(filename)
	# convert to integer
	filesize = int(filesize)
	progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
	with open(filename, "wb") as f:
		while True:
		# read 1024 bytes from the socket (receive)
			bytes_read = conn.recv(BUFFER_SIZE)
			if not bytes_read:    
            # nothing is received
            # file transmitting is done
				break
        # write to the file the bytes we just received
			f.write(bytes_read)
        # update the progress bar
			progress.update(len(bytes_read))

def main():
    create_socket()
    bind_socket()
    socket_accept()


main()