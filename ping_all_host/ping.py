import os

with open("D:\\mylist\\iplist.txt") as file:
	dump = file.read()
	dump = dump.splitlines()
print(dump)
for i in dump:
	ip = i.split()[0]
	host = i.split()[0]
	print(ip)
	res = os.popen(f"ping {ip} -n 2").read()
	if "Request timed out" in res:
		print(res)
	elif "Destination host unreachable" in res:
		print(res)
	else:
		print(res)
	