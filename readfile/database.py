import os, time
import mysql.connector
from os.path import join, getsize


mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="tree"
)

mycursor = mydb.cursor()
try:
	mycursor.execute("CREATE TABLE etc (id INT AUTO_INCREMENT PRIMARY KEY, parent VARCHAR(255), name VARCHAR(255), type VARCHAR(255), size INT(255), date_create VARCHAR(255), date_last_modified VARCHAR(255))")
except mysql.connector.errors.ProgrammingError as e:
	pass


for foldername, subfolders, filenames in os.walk('etc'):

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
		sql = "INSERT INTO etc (parent,name,type,size,date_create,date_last_modified) VALUES (%s,%s,%s,%s,%s,%s)"
		val = (parent,subfolder,"folder",size,create,last_modified)
		mycursor.execute(sql, val)
		mydb.commit()
	for filename in filenames:
		# print('FILE INSIDE ' + foldername+':'+filename)
		path = join(foldername,filename)
		size = getsize(path)
		last_modified = time.ctime(os.path.getmtime(path))
		create = time.ctime(os.path.getctime(path))
		sql = "INSERT INTO etc (parent,name,type,size,date_create,date_last_modified) VALUES (%s,%s,%s,%s,%s,%s)"
		val = (parent,filename,"file",size,create,last_modified)
		mycursor.execute(sql, val)
		mydb.commit()