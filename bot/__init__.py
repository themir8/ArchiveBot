import sys
import telebot
from loguru import logger
from config.config import token
# from model.postgres import DataBase # for postgres
from model.sqlite import DataBase # for sqlite


bot = telebot.TeleBot(token)


# db = DataBase() # for posgres
db = DataBase("sqlite.db") # for sqlite


# logging
logger.add(sys.stderr, format="{time} {message}", filter="my_module", level="INFO")
tb = bot.get_me()
logger.info("{} is connected", tb.first_name)