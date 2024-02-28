from translaterate import to_cyrillic,to_latin
import telebot
TOKEN= "7158593237:AAG4CVpVs6-2omwKXX__AfpapniPISPeJms"
bot = telebot.TeleBot(TOKEN,parse_mode=None)
@bot.message_handler(commands = ["start"])
def send_welcome(message):
    toUser = "Assalomu aleykom xush kelibsiz"
    toUser += "\nMatn kiritng:"
    bot.reply_to(message, toUser )

@bot.message_handler(func = lambda message: True)
def echo_all (message):
    msg = message.text
    if msg.isascii():
        answer = to_cyrillic(msg)
    else:
        answer = to_latin(msg)
    bot.reply_to(message,answer)

bot.polling()
    