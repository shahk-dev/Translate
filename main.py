from transliterate import to_latin, to_cyrillic
import telebot

Token = '8209354448:AAEG7I9Dib3Dd9D6eT0fasiBMrKJ7zXMhj4'
bot = telebot.TeleBot(Token, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = "Assalomu alaykum! Siz Shahkweb tomonidan yaratilgan botga xush kelibsiz 😜"
    javob += "\nMatn kiriting:"
    bot.reply_to(message, javob)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text

    if msg.isascii():
        javob = to_cyrillic(msg)
    else:
        javob = to_latin(msg)

    bot.reply_to(message, javob)

bot.infinity_polling()
