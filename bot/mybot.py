import telebot
import os
import subprocess

bot = telebot.TeleBot("1880360296:AAFzuqt9LHjps6czoU0-WA4i2VNarR7cjkk", parse_mode=None)
chat_id = 1537849994


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "/ram ==== display the total amount of memory"
					+"\n"+"/os  ==== display version OS"
					+"\n"+"/hw  ==== displays the amount of disk space")

@bot.message_handler(commands=['os'])
def display_version_os(message):
	commands = ['cat','/etc/os-release'] 
	result = subprocess.check_output(commands,stderr=subprocess.STDOUT)
	bot.reply_to(message, result.decode())


#kiem tra RAM
@bot.message_handler(commands=['ram'])
def display_total_ram(message):
	commands = ['free','-h']
	result = subprocess.check_output(commands,stderr=subprocess.STDOUT)
	bot.reply_to(message, result.decode())

@bot.message_handler(commands=['hw'])
def display_disk_space(message):
	commands = ['df','-h']
	result = subprocess.check_output(commands,stderr=subprocess.STDOUT)
	bot.reply_to(message, result.decode())

def tree_dir(message):
	request = message.text.split()
	if len(request) < 2 or request[0].lower() not in "tree":
		return False
	else:
		return True

@bot.message_handler(func=tree_dir)
def res_tree(message):
	directory = message.text.split()[1]
	request = ['tree',directory,'-f','-pug','-h','-D','-o','direc_tree.txt']
	result = subprocess.check_output(request,stderr=subprocess.STDOUT)
	doc = open('direc_tree.txt','rb')
	bot.send_document(chat_id, doc)

bot.polling()