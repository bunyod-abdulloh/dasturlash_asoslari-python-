from kirill_lotin_bot.data import BOT_TOKEN
from transliterate import to_cyrillic, to_latin
import telebot

bot = telebot.TeleBot(BOT_TOKEN, parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = "Assalomu alaykum! Xush kelibsiz!\n"
    javob += "Matn kiriting"
    bot.reply_to(
        message, javob
    )


@bot.message_handler(func=lambda message: True)
def transliterate_message(message):
    msg = message.text

    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)

    bot.reply_to(
        message=message, text=javob(msg)
    )


bot.polling()
