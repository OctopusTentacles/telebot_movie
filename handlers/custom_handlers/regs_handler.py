"""
Модуль кнопки ЗАРЕГИСТРИРОВАТЬСЯ.

Этот модуль содержит обработчик кнопки регистрации пользователя.
"""


from database import save_user_registration
from handlers.default_handlers.start import bot_start
from loader import bot
from log_data import logger
from states.user_input import UserInputState
from telebot.types import CallbackQuery


@bot.callback_query_handler(func=lambda call: call.data == 'register')
def register_user(call: CallbackQuery):
    """
    Обработчик нажатия кнопки регистрации.

    Эта функция вызывается при нажатии пользователем кнопки "Зарегистрироваться".
    Она устанавливает состояние пользователя в режим регистрации,
    сохраняет информацию о пользователе в базе данных при успешной регистрации,
    и вызывает функцию bot_start для продолжения работы с пользователем.

    Args:
        call (CallbackQuery): Объект, представляющий вызов 
                                обратного запроса от пользователя.

    Returns:
        None
    """
    bot.set_state(call.message.chat.id, UserInputState.register)

    current_state = bot.get_state(call.message.chat.id)
    logger.info(f'Current state: {current_state}')

    user_id = call.from_user.id
    user_name = call.from_user.full_name
    
    if save_user_registration(user_id, user_name):
        logger.info(
            f'User {user_name} with ID {user_id} successfully registered.'
        )
        bot.send_message(
            call.message.chat.id, 'Вы успешно зарегистрированы!'
        )

        # После успешной регистрации вызываем функцию bot_start:
        bot.send_message(
            call.message.chat.id, 'Нажмите /start'
        )
        
    else:
        bot.send_message(
            call.message.chat.id,
            'Что-то пошло не так...Начни сначала '
        )
