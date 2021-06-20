import os

with open("list_ip.txt") as file:
	dump = file.read()
	dump = dump.splitlines()
print(dump)
for i in dump:
	ip = i.split()[0]
	host = i.split()[0]
	print(ip)
	res = os.popen(f"ping {ip} -n 2").read()
	if "Request timed out" in res:
		print("down")
	elif "Destination host unreachable" in res:
		print("down")
	else:
		print("up")
	