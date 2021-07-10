import re
f = open("direc_tree.txt", "r")

for x in f:

	# print(x)
	# a = re.findall("\Aâ”œâ”€â”€",x)
	# if a:
	# 	print(x)
	try:

		a = x.split("]  /")
		print(a[1])
	
	except IndexError as e:
		pass

	# a = re.search(r"/etc",x)
	# print(a.string)

	# a = re.findall("^].*\n$")
	# if a:
	# 	print


# con trực tiếp â””â”€â”€
# con của con â”‚Â Â  â”œâ”€â”€
# con của con của con â”‚Â Â      â”œâ”€â”€