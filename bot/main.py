#!/usr/bin/python3

import telebot
# from telebot.types import Message
from config.config import token

bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def welc(message):
    """ This func for registrated users """

    # welcome message
    bot.send_message(
        message.chat.id,
        "Salom <b>{0.first_name}</b> \nMen - <b>{1.first_name}</b> man.\n<b>Bizning Kanal: </b> <a href='https://t.me/joinchat/AAAAAFbI79pDC_7LkK2BXA'>Python blog</a> <b>!!!</b>"
        .format(message.from_user, bot.get_me()),
        parse_mode='html')


# @bot.message_handler(commands=["python"])
# def python_about(message: Message):
# 	""" This func for registrated users """

# 	text = "Python ingiliz tiliga o'hshab oddiy o'qiladi python dasturlash tili c++ dasturlsh tilida yozilgan bo'lib uni buyuk dasturchi 'Gvido Van Rossum'-yaratgan.\n\
# 			Python dasturlash tilining nomi umuman ilonlar ismidan olinmagan pythonni yozgan dasturchi bir kulgili shouni nomidan ko'chirgan shouning oti esa 'Monti pythonning uchar tsirki'-edi."

# 	bot.send_message(message.chat.id, text,
# 		parse_mode='html')

# @bot.message_handler(commands=["about"])
# def about(message: Message):
# 	""" This func for registrated users """

# 	text = "Men o'zbek programistlariga yordam berish uchun yaratilgan botman"

# 	bot.send_message(message.chat.id, text,
# 		parse_mode='html')

# @bot.message_handler(content_types=['text'])
# @bot.edited_message_handler(content_types=['text'])
# def text(message: Message):

# 	if message.chat.id in Mirsaid and '#mir' in message.text:
# 		bot.send_message(message.chat.id, "Salom, Boss")

# 	elif "Orqaga qaytish" in message.text:
# 		bot.send_message(message.chat.id, "Bosh menyu", reply_markup=main_btn)

# 	elif "📚Python darsliklar" in message.text:
# 		bot.send_message(message.chat.id, "Qanaqa mavzuda dagi dars?", reply_markup=python_main_btn)

# 	elif "Python-sintaksis" in message.text:
# 		bot.send_message(message.chat.id, "Python 1-dars Malumotlar turlari <a href='https://telegra.ph/Python-boyicha-dars-1-Malumotlar-turlari-05-24'>Malumotlar turlari</a>",
# 			parse_mode='html')

# 		bot.send_message(message.chat.id, "Python 2-dars <a href='https://telegra.ph/Python-boyicha-2-dars-Operatorlar-va-tsikllar-05-25'>Operatlar va tsikllar</a>",
# 			parse_mode='html')

# 	elif "📣📣Foydali kanal va gruppalar!" in message.text:
# 		bot.send_message(message.chat.id, foydali_kanallar,
# 			parse_mode='html')

# 	elif "Bot info🤔" in message.text:
# 		text = "Men o'zbek programistlariga yordam berish uchun yaratilgan botman"

# 		bot.send_message(message.chat.id, text,
# 			parse_mode='html')

# 	elif "👨🏻‍💻Creator haqida ma'lumot!" in message.text:
# 		bot.send_message(message.chat.id, crator,
# 			parse_mode='html')

try:
    if __name__ == '__main__':
        bot.infinity_polling()
except Exception as e:
    with open("Teacher_robot/dat/erorr.log", "a") as erorr:
        log = erorr.load()
