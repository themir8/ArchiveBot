from __init__ import db
from telebot.types import ReplyKeyboardMarkup, KeyboardButton


################################## Exit Button
exit_btn = ReplyKeyboardMarkup(resize_keyboard=True).add("Orqaga")




################################## Main Button
main_btn = ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = KeyboardButton("Library 📚")
btn2 = KeyboardButton("Playlist 🎵")
btn3 = KeyboardButton("Pictures 📷")
main_btn.row(btn1, btn2, btn3)




################################## Library Menu Button
libr_menu_btn=ReplyKeyboardMarkup(resize_keyboard=True)
btn1=KeyboardButton("Books")
btn2=KeyboardButton("Add book")
# btn3=KeyboardButton("Remove book")
libr_menu_btn.row(btn1, btn2)




################################## Playlist Menu Button
playlist_menu_btn=ReplyKeyboardMarkup(resize_keyboard=True)
btn1=KeyboardButton("All musics")
btn2=KeyboardButton("Add music")
# btn3=KeyboardButton("Remove music")
playlist_menu_btn.row(btn1, btn2)




################################## Library Button
button = db.get_all_books()
data = {'list': []}


for i in button:
    data['list'].append({'name': i[1]})
    # print(data)

book_button = ReplyKeyboardMarkup(
    resize_keyboard=True, row_width=2)
for i in range(len(data['list'])):
    button = KeyboardButton(data['list'][i]['name'])
    book_button.add(button)
book_button.add("Orqaga")




################################## Music Button
button = db.get_all_musics()
data = {'list': []}


for i in button:
    data['list'].append({'name': i[1]})

music_button = ReplyKeyboardMarkup(
    resize_keyboard=True, row_width=2)
for i in range(len(data['list'])):
    button = KeyboardButton(data['list'][i]['name'])
    music_button.add(button)
music_button.add("Orqaga")