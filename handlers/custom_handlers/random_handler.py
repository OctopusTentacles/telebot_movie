"""Модуль команды rand из кнопки ГЛАВНОГО МЕНЮ Рандом."""


from api import random_films_api
from api import random_serials_api
from api import random_cartoons_api

from keyboards.inline import type_keyboard
from loader import bot
from log_data import logger
from states.user_input import UserInputState
from telebot.types import CallbackQuery


