"""Модуль используется для установки стандартных команд бота. 
Он импортирует BotCommand из telebot.types,
использует set_my_commands для установки команд.
"""


from telebot.types import BotCommand
from config_data.config import DEFAULT_COMMANDS
from config_data.config import CUSTOM_COMMANDS


def set_default_commands(bot):
    bot.set_my_commands(
        [BotCommand(*i) for i in DEFAULT_COMMANDS]
    )

def set_custom_commands(bot):
    bot.set_my_commands(
        [BotCommand(*i) for i in CUSTOM_COMMANDS]
    )
    