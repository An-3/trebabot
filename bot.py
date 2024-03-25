import telebot

bot = telebot.TeleBot('6298227780:AAFnkm0KdmQAx5d24Jg8_JMrWH0s5vRDg_A')

bot.set_webhook()


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()
