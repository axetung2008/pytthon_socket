import time as t
import socket
##this will enable to utilize specified functions within time library such as sleep()
#time countdown 
seconds = 30

def port():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	address = '168.138.53.103'

	port = [80,43,2222]
	for p in port:
		result = sock.connect_ex((address,p))
		if result == 0:
		   # print ("Port is open")
		   print("{} is open".format(p))
		else:
		   # print (p + "Port is not open")
		   print("{} is not open".format(p))
		sock.close()

while True:
	for i in range(seconds):
		print(str(seconds-i) + " seconds remaining \n")
		t.sleep(1)
	port()
	print("Time is up")
##we also need the loop to wait for 1 second between each iteration
