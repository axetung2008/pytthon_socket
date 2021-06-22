import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
add = '168.138.53.50'

port = 80
result = sock.connect_ex((add,port))
if result == 0:
   print ("Port is open")
else:
   print ("Port is not open")
sock.close()