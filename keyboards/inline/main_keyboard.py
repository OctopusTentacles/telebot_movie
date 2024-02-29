"""Модуль основных кнопок бота. Главное меню."""


from telebot.types import InlineKeyboardButton
from telebot.types import InlineKeyboardMarkup


def main_keyboard():
    """Возвращает основную клавиатуру.

    Returns:
        types.InlineKeyboardMarkup: Объект основной клавиатуры.
    """
    keyboard = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton(text='Популярное', callback_data='pop')
    button_2 = InlineKeyboardButton(text='Ожидаемое', callback_data='await')
    button_3 = InlineKeyboardButton(text='Новинки', callback_data='new')
    button_4 = InlineKeyboardButton(text='Рандом', callback_data='rand')
    button_5 = InlineKeyboardButton(text='Поиск фильма', callback_data='movie')
    button_6 = InlineKeyboardButton(text='Поиск фильма', callback_data='person')

    keyboard.add(button_1, button_2, button_3, button_4, button_5, button_6)

    return keyboard
