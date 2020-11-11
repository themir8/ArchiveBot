import sys
import telebot
from loguru import logger
from config.config import token
from model.db import DataBase


bot = telebot.TeleBot(token)
db = DataBase()
# logging
logger.add(sys.stderr, format="{time} {message}", filter="my_module", level="INFO")
tb = bot.get_me()
logger.info("{} is connected", tb.first_name)