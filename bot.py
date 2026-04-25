import telebot
from telebot import types

TOKEN = "8792919855:AAEERO2kra7TbCMB6s2XUqZB2ciT_NMBp7I"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton('🚀 بدء الكراش')
    btn2 = types.KeyboardButton('👨‍💻 المطور')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "🔥 تم تشغيل بوت الكراش بنجاح على السيرفر!", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle(message):
    if message.text == '👨‍💻 المطور':
        bot.reply_to(message, "المطور: عبد الباسط إبراهيم 🇾🇪")
    else:
        bot.reply_to(message, "جاري المعالجة... ⚡")

bot.infinity_polling()

