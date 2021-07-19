#==========this script only run on LINUX================
import os, time
import mysql.connector
from os.path import join, getsize
from pathlib import Path

mydb = mysql.connector.connect(
	host="168.138.53.103",
	user="admin",
	password="admin123",
	database="tree_folder"
)

mycursor = mydb.cursor()
try:
	mycursor.execute("CREATE TABLE etc (id INT AUTO_INCREMENT PRIMARY KEY, parent VARCHAR(255), name VARCHAR(255), type VARCHAR(255), size INT(255), owner_user VARCHAR(255), group_user VARCHAR(255), date_create VARCHAR(255), date_last_modified VARCHAR(255))")
except mysql.connector.errors.ProgrammingError as e:
	pass


for foldername, subfolders, filenames in os.walk('/etc'):
	try:
		# print('The Current folder is: ' + foldername)
		directory = os.listdir(foldername)
		if len(directory) == 0:
			continue
		else:
			parent = foldername
		for subfolder in subfolders:
			# print(' SUBFOLDER OF ' + foldername +':'+subfolder)
			path = join(foldername,subfolder)
			size = getsize(path)
			last_modified = time.ctime(os.path.getmtime(path))
			create = time.ctime(os.path.getctime(path))
			owner = Path(path).owner()
			group = Path(path).group()
			sql = "INSERT INTO etc (parent,name,type,size,owner_user,group_user,date_create,date_last_modified) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
			val = (parent,subfolder,"folder",size,owner,group,create,last_modified)
			mycursor.execute(sql, val)
			mydb.commit()
		for filename in filenames:
			# print('FILE INSIDE ' + foldername+':'+filename)
			path = join(foldername,filename)
			size = getsize(path)
			last_modified = time.ctime(os.path.getmtime(path))
			create = time.ctime(os.path.getctime(path))
			owner = Path(path).owner()
			group = Path(path).group()
			sql = "INSERT INTO etc (parent,name,type,size,owner_user,group_user,date_create,date_last_modified) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
			val = (parent,subfolder,"folder",size,owner,group,create,last_modified)
			mycursor.execute(sql, val)
			mydb.commit()
	except FileNotFoundError as e:
		continue

# sql = "INSERT INTO etc (parent,name,type,size,date_create,date_last_modified) VALUES (%s,%s,%s,%s,%s,%s)"
# val = ("parent","subfolder","folder",4,"create","last_modified")
# mycursor.execute(sql, val)
# mydb.commit()