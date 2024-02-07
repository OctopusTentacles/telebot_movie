"""Модуль выбора типа контента. Подменю."""


from telebot.types import InlineKeyboardButton
from telebot.types import InlineKeyboardMarkup


def type_keyboard():
    """Возвращает дополнительную клавиатуру.

    Returns:
        types.InlineKeyboardMarkup: Объект доп. клавиатуры.
    """
    keyboard = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton(text='фильмы', callback_data='film')
    button_2 = InlineKeyboardButton(text='сериалы', callback_data='serial')
    button_3 = InlineKeyboardButton(text='мультфильмы', callback_data='cartoon')

    keyboard.add(button_1, button_2, button_3)

    return keyboard
