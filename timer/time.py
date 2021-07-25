import time as t
import socket
##this will enable to utilize specified functions within time library such as sleep()
#time countdown 
seconds = 5

ip_add = "168.138.53.103"

#List port to check
list_port = [25 ,80, 111, 465, 587, 3306, 555]
open_ports = []
def scan_port():

	#List port is open

	#Convert list to set
	set_of_list_port = set(list_port)

	#Loop if port is open append to list open_port
	for port in list_port:

		try:
		    
		    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		        
		        s.settimeout(0.5)
		        
		        s.connect((ip_add, port))
		        
		        open_ports.append(port)

		except:
		    
		    pass

	#Conver list to set
	set_of_open_ports = set(open_ports)

	#Difference two of sets
	set_temp = set_of_list_port.difference(set_of_open_ports)

	result = list(set_temp)
	if result:
		for i in result:
			print(f"Port {i} is not open.")
	else:
		print("All port is open!")

while True:
	for i in range(seconds):
		print(str(seconds-i) + " seconds remaining \n")
		t.sleep(1)
	print(ip_add)
	scan_port()
