import telebot
import os
import subprocess
import time as t
import socket

bot = telebot.TeleBot("1880360296:AAFzuqt9LHjps6czoU0-WA4i2VNarR7cjkk", parse_mode=None)
chat_id = 1537849994

#Time to reply
seconds = 300

ip_add = "168.138.53.103"

#List port to check
list_port = [25 ,80, 111, 465, 587, 3306]
open_ports = []
def test_send_message():
	set_of_list_port = set(list_port)
	for port in list_port:

		try:

			with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

				s.settimeout(0.5)

				s.connect((ip_add, port))

				open_ports.append(port)

		except:
		# We don't need to do anything here. If we were interested in the closed ports we'd put something here.
			pass

	#Conver list to set
	set_of_open_ports = set(open_ports)

	#Difference two of sets
	set_temp = set_of_list_port.difference(set_of_open_ports)

	result = list(set_temp)
	if result:
		for i in result:
			text =f"Port {i} is not open."
	else:
		text = "All port is open!"
	ret_msg = bot.send_message(chat_id, text)
	assert ret_msg.message_id
	print(text)
while True:
	for i in range(seconds):
		t.sleep(1)
	
	test_send_message()


#========================================================
# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
# 	bot.reply_to(message, "/ram ==== display the total amount of memory"
# 					+"\n"+"/os  ==== display version OS"
# 					+"\n"+"/hw  ==== displays the amount of disk space")

# @bot.message_handler(commands=['os'])
# def display_version_os(message):
# 	commands = ['cat','/etc/os-release'] 
# 	result = subprocess.check_output(commands,stderr=subprocess.STDOUT)
# 	bot.reply_to(message, result.decode())


# #kiem tra RAM
# @bot.message_handler(commands=['ram'])
# def display_total_ram(message):
# 	commands = ['free','-h']
# 	result = subprocess.check_output(commands,stderr=subprocess.STDOUT)
# 	bot.reply_to(message, result.decode())

# @bot.message_handler(commands=['hw'])
# def display_disk_space(message):
# 	commands = ['df','-h']
# 	result = subprocess.check_output(commands,stderr=subprocess.STDOUT)
# 	bot.reply_to(message, result.decode())

# def tree_dir(message):
# 	request = message.text.split()
# 	if len(request) < 2 or request[0].lower() not in "tree":
# 		return False
# 	else:
# 		return True

# @bot.message_handler(func=tree_dir)
# def res_tree(message):
# 	directory = message.text.split()[1]
# 	request = ['tree',directory,'-f','-pug','-h','-D','-o','direc_tree.txt']
# 	result = subprocess.check_output(request,stderr=subprocess.STDOUT)
# 	doc = open('direc_tree.txt','rb')
# 	bot.send_document(chat_id, doc)

bot.polling()