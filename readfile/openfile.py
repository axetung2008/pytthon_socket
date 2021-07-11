import re

class TreeNode:
	def __init__(self, data):
		self.data = data
		self.children = []
		self.parent = None

	def get_level(self):
		level = 0
		p = self.parent
		while p:
		    level += 1
		    p = p.parent

		return level

	def print_tree(self):
		spaces = ' ' * self.get_level() * 3
		prefix = spaces + "|__" if self.parent else ""
		print(prefix + self.data)
		if self.children:
		    for child in self.children:
		        child.print_tree()

	def add_child(self, child):
		child.parent = self
		self.children.append(child)
# def build_product_tree():
# 	#Electronics/Laptop
# 	#Electronics/Laptop/Mac
# 	#Electronics/Laptop/Surface
# 	#Electronics/Laptop/Thinkpad
#     root = TreeNode("Electronics")

#     laptop = TreeNode("Laptop")
#     laptop.add_child(TreeNode("Mac"))
#     laptop.add_child(TreeNode("Surface"))
#     laptop.add_child(TreeNode("Thinkpad"))

#     cellphone = TreeNode("Cell Phone")
#     cellphone.add_child(TreeNode("iPhone"))
#     cellphone.add_child(TreeNode("Google Pixel"))
#     cellphone.add_child(TreeNode("Vivo"))

#     tv = TreeNode("TV")
#     tv.add_child(TreeNode("Samsung"))
#     tv.add_child(TreeNode("LG"))

#     root.add_child(laptop)
#     root.add_child(cellphone)
#     root.add_child(tv)

#     root.print_tree()

# if __name__ == '__main__':
#     build_product_tree()


f = open("direc_tree.txt", "r")

first_line = f.readline()
newline = re.sub("/","",first_line)
root = re.sub("\n","",newline)


dic_id = {}
dic_parent_id = {}
direc_tree = {}
index = 1

dic_parent_id[root]=-1
dic_id[0]=root
for x in f:

# # 	# print(x)
# # 	# a = re.findall("\Aâ”œâ”€â”€",x)
# # 	# if a:
# # 	# 	print(x)
	try:

		a = x.split("]  /")
		# arr = a[1].split("/")
		path = re.sub("\n","",a[1])

		dic_id[index]=path
		dic_parent_id[path]=0 
		index = index + 1
	except IndexError as e:
		pass
	
	# a = re.search(r"/etc",x)
	# print(a.string)

	# a = re.findall("^].*\n$")
	# if a:
	# 	print

# while True:
# 	for x,y in 
for x,y in dic_id.items():
	

# con trực tiếp â””â”€â”€
# con của con â”‚Â Â  â”œâ”€â”€
# con của con của con â”‚Â Â      â”œâ”€â”€

