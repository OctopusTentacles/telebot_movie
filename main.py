from loader import bot
import handlers
from utils.set_bot_commands import set_default_commands
from utils.set_bot_commands import set_custom_commands


if __name__ == '__main__':
    set_default_commands(bot)
    set_custom_commands(bot)
    bot.infinity_polling()

 
# TODO 
    # ДОБАВИТЬ ПОДМЕНЮ В ПОПуляном
