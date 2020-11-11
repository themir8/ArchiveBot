from telebot.types import Message
from config.config import admin
from config.texts import *
from button import music_button, book_button, main_btn, libr_menu_btn, playlist_menu_btn, exit_btn
from __init__ import bot, db



# Bussines logic
@bot.message_handler(func=lambda message: message.chat.id in admin, commands=["start"])
def welc(message: Message):
    user_id = message.from_user.id
    
    # hello message
    msg=bot.send_message(
            user_id,
            hello_message_for_lord,
            reply_markup=main_btn,
            parse_mode='html')
    bot.register_next_step_handler(msg, main_handler)


def main_handler(message: Message):
    user_id = message.from_user.id
    if message.text == "Library 📚":
        msg=bot.send_message(
            user_id,
            "Ok :)",
            reply_markup=libr_menu_btn)
        bot.register_next_step_handler(msg, libr_menu)

    elif message.text == "Playlist 🎵":
        msg=bot.send_message(
            user_id,
            "Ok :)",
            reply_markup=playlist_menu_btn)
        bot.register_next_step_handler(msg, playlist_menu)
    
    # elif message.text == "Pictures 📷":
    #     pass




######################################## Library menu
def libr_menu(message):
    user_id = message.from_user.id

    if message.text == "Books":
        msg = bot.send_message(user_id, "List of books:", reply_markup=book_button)
        bot.register_next_step_handler(msg, get_single_book)
    
    elif message.text == "Add book":
        msg = bot.send_message(user_id, 
            "Send me a book",
            reply_markup=exit_btn)
        bot.register_next_step_handler(msg, handle_docs)


def get_single_book(message: Message):
    user_id = message.from_user.id
    if message.text == "Orqaga":
        msg=bot.send_message(
            user_id,
            hello_message_for_lord,
            reply_markup=main_btn,
            parse_mode='html')
        bot.register_next_step_handler(msg, main_handler)
    else:
        book = db.get_book(message.text)
        try:
            msg = bot.send_document(user_id, book[0][2])
            bot.register_next_step_handler(msg, get_single_book)
        except Exception as e:
            print(e)
            msg = bot.send_message(user_id, "List of books:", reply_markup=book_button)
            bot.register_next_step_handler(msg, get_single_book)
    

def handle_docs(message):
    user_id = message.from_user.id
    
    if message.text == "Orqaga":
        msg=bot.send_message(
            user_id,
            hello_message_for_lord,
            reply_markup=main_btn,
            parse_mode='html')
        bot.register_next_step_handler(msg, main_handler)

    elif message.content_type == 'document':
        db.add_book(file_name=message.document.file_name, file_id=message.document.file_id)
        try:
            bot.send_message(user_id, "Saved!")

            msg=bot.send_message(
                user_id,
                hello_message_for_lord,
                reply_markup=main_btn,
                parse_mode='html')
            bot.register_next_step_handler(msg, main_handler)
        except Exception as e:
            bot.send_message(user_id, str(e))

            msg=bot.send_message(
                user_id,
                hello_message_for_lord,
                reply_markup=main_btn,
                parse_mode='html')
            bot.register_next_step_handler(msg, main_handler)
    else:
        bot.send_message(user_id, 
            "<b>Error: </b> <code>Message format not a document!</code>",
            parse_mode='html')
        msg = bot.send_message(user_id, 
            "Send me a <b>book!</b>",
            reply_markup=exit_btn,
            parse_mode='html')
        bot.register_next_step_handler(msg, handle_docs)




######################################## Playlist menu
def playlist_menu(message):
    user_id = message.from_user.id

    if message.text == "All musics":
        msg = bot.send_message(user_id, "List of musics:", reply_markup=music_button)
        bot.register_next_step_handler(msg, get_single_music)
    
    elif message.text == "Add music":
        msg = bot.send_message(user_id, 
            "Send me a music",
            reply_markup=exit_btn)
        bot.register_next_step_handler(msg, add_music)


def get_single_music(message: Message):
    user_id = message.from_user.id
    if message.text == "Orqaga":
        msg=bot.send_message(
            user_id,
            hello_message_for_lord,
            reply_markup=main_btn,
            parse_mode='html')
        bot.register_next_step_handler(msg, main_handler)
    else:
        music = db.get_music(message.text)
        try:
            msg = bot.send_audio(user_id, music[0][2])
            bot.register_next_step_handler(msg, get_single_music)
        except Exception as e:
            print(e)
    

def add_music(message):
    user_id = message.from_user.id

    if message.text == "Orqaga":
        msg=bot.send_message(
            user_id,
            hello_message_for_lord,
            reply_markup=main_btn,
            parse_mode='html')
        bot.register_next_step_handler(msg, main_handler)

    elif message.content_type == 'audio':
        db.add_music(file_name=message.json['audio']['file_name'], file_id=message.json['audio']['file_id'])
        try:
            bot.send_message(user_id, "Saved!")

            msg=bot.send_message(
                user_id,
                hello_message_for_lord,
                reply_markup=main_btn,
                parse_mode='html')
            bot.register_next_step_handler(msg, main_handler)
        except Exception as e:
            bot.send_message(user_id, str(e))

            msg=bot.send_message(
                user_id,
                hello_message_for_lord,
                reply_markup=main_btn,
                parse_mode='html')
            bot.register_next_step_handler(msg, main_handler)
    else:
        bot.send_message(user_id, 
            "<b>Error: </b> <code>Message format not a audio!</code>",
            parse_mode='html')
        msg = bot.send_message(user_id, 
            "Send me a <b>music!</b>",
            reply_markup=exit_btn,
            parse_mode='html')
        bot.register_next_step_handler(msg, add_music)


bot.enable_save_next_step_handlers(delay=2)

bot.load_next_step_handlers()



try:
    if __name__ == '__main__':
        bot.infinity_polling()
except Exception:
    db.close()
