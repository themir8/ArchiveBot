#!/usr/bin/python3
from telebot.types import Message
from config.config import admin
from config.texts import *
from button import music_button, book_button
from __init__ import bot, db



# Bussines logic
@bot.message_handler(func=lambda message: message.chat.id in admin, commands=["start"])
def welc(message: Message):
    user_id = message.from_user.id
    
    # hello message
    bot.send_message(
        user_id,
        hello_message_for_lord,
        parse_mode='html')


@bot.message_handler(func=lambda message: message.chat.id in admin, commands=["newbook"])
def newbook(message: Message):
    user_id = message.from_user.id
    msg = bot.send_message(user_id, "Send me a book")
    bot.register_next_step_handler(msg, handle_docs)


@bot.message_handler(func=lambda message: message.chat.id in admin, content_types=['document'])
def handle_docs(message):
    user_id = message.from_user.id
    db.add_book(file_name=message.document.file_name, file_id=message.document.file_id)
    try:
        bot.send_message(user_id, "Saved!")
    except Exception as e:
        bot.send_message(user_id, str(e))


@bot.message_handler(func=lambda message: message.chat.id in admin, commands=['library'])
def handle_archive(message):
    user_id = message.from_user.id
    
    msg = bot.send_message(user_id, "List of books:", reply_markup=book_button)
    bot.register_next_step_handler(msg, get_single_book)


def get_single_book(message: Message):
    user_id = message.from_user.id
    book = db.get_book(message.text)
    try:
        msg = bot.send_document(user_id, book[0][2])
        bot.register_next_step_handler(msg, get_single_book)
    except Exception as e:
        bot.send_message(user_id, "Error: "+str(e))
        # hello message
        msg = bot.send_message(
                user_id,
                hello_message_for_lord,
                parse_mode='html')
        bot.register_next_step_handler(msg, welc)


@bot.message_handler(func=lambda message: message.chat.id in admin, commands=["newmusic"])
def newmusic(message: Message):
    user_id = message.from_user.id
    msg = bot.send_message(user_id, "Send me a music")
    bot.register_next_step_handler(msg, handle_music)


@bot.message_handler(func=lambda message: message.chat.id in admin, content_types=['audio'])
def handle_music(message):
    # print(message.json['audio']['file_name'])
    user_id = message.from_user.id
    db.add_music(file_name=message.json['audio']['file_name'], file_id=message.json['audio']['file_id'])
    try:
        bot.send_message(user_id, "Saved!")
    except Exception as e:
        bot.send_message(user_id, str(e))


@bot.message_handler(func=lambda message: message.chat.id in admin, commands=['playlist'])
def handle_playlist(message):
    user_id = message.from_user.id
    
    msg = bot.send_message(user_id, "List of books:", reply_markup=music_button)
    bot.register_next_step_handler(msg, get_single_music)


def get_single_music(message: Message):
    user_id = message.from_user.id
    music = db.get_music(message.text)
    try:
        msg = bot.send_audio(user_id, music[0][2])
        bot.register_next_step_handler(msg, get_single_music)
    except Exception as e:
        bot.send_message(user_id, "Error: "+str(e))
        # hello message
        msg = bot.send_message(
                user_id,
                hello_message_for_lord,
                parse_mode='html')
        bot.register_next_step_handler(msg, welc)


@bot.message_handler(func=lambda message: message.chat.id in admin, content_types=['text'])
@bot.edited_message_handler(func=lambda message: message.chat.id in admin, content_types=['text'])
def text(message: Message):
    user_id = message.from_user.id
    lowercase = message.text.lower()
    if lowercase == "i'm admin":
        bot.send_message(user_id, "Hello admin")

    if lowercase == "show me the admin panel":
        bot.send_message(user_id, "Here it is")




try:
    if __name__ == '__main__':
        bot.infinity_polling()
except Exception:
    db.close()
