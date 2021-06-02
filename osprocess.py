import subprocess
import os
import sys
#command = input()
# result = subprocess.check_output('pwd')

# subprocess.Popen("ls", cwd='/')





while True:
	a = input()

	x = a.split()

	if x[0] == "pwd" or x[0] == "ls":
		pwd = os.getcwd()
		print(pwd)
		subprocess.run(['ls','-l'])
		continue
	# Change the current working directory
	if x[0] == "cd":
		os.chdir(x[1])
		print(os.getcwd())
		continue
	try:
		output = subprocess.check_output(a, stderr=subprocess.STDOUT)
		print(output.decode())
	except FileNotFoundError as e:
		print("Command not found. Please try again!")
	# result = subprocess.check_output(a)
	# print(result.decode())
	
# command = ["lslk", "-l"]
# try:
#     output = subprocess.check_output(command, stderr=subprocess.STDOUT).decode()

# except FileNotFoundError as e:
#     print("Command not found. Please try again!")




# print(x)

