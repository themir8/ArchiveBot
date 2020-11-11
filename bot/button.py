from __init__ import db
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

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