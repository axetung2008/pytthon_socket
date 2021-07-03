import telebot
import os

bot = telebot.TeleBot("1880360296:AAFzuqt9LHjps6czoU0-WA4i2VNarR7cjkk", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

bot.polling()