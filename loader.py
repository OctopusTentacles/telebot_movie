"""Модуль для подгрузки переменных."""


from telebot import TeleBot
from telebot.storage import StateMemoryStorage
from config_data import config

# глобальая переменная для хранения:
storage = StateMemoryStorage()
bot = TeleBot(token=config.BOT_TOKEN, state_storage=storage)