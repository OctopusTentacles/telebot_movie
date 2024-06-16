""" Модуль проверки регистрации пользователей. """


from datetime import datetime
from log_data import logger
from .models import UserRegistration


def check_user_registration(user_id: int):
    """Проверяет, зарегистрирован ли пользователь.

    Args:
        user_id (int): Идентификатор пользователя.

    Returns:
        bool: True, если пользователь зарегистрирован, False в противном случае.
    """
    return UserRegistration.select().where(
        UserRegistration.user_id == user_id).exists()


def save_user_registration(user_id: int, user_name: str) -> bool:
    """Сохраняет регистрацию пользователя в базе данных.

    Args:
        user_id (int): Идентификатор пользователя.
        user_name (str): Имя пользователя.

    Returns:
        bool: True, если регистрация прошла успешно,
              False в противном случае.
    """
    try:
        new_user = UserRegistration.create(
            user_id=user_id,
            user_name=user_name,
            favorite_movies='',
            registration_date=datetime.now()
        )
        return True

    except Exception as exc:
        logger.error(
            f'Ошибка при сохранении регистрации пользователя {user_id}: {exc}'
        )
        return False
    

def get_user_name(user_id):
    try:
        user = UserRegistration.select().where(
            UserRegistration.user_id == user_id).first()
        if user:
            return user.user_name
        
    except Exception as exc:
        logger.error(
            f'Ошибка, пользователь отсутствует в базе: {exc}'
        )

def add_favorite_movie(user_id: int, movie_name: str) -> bool:
    """Добавляет фильм в избранное пользователя.

    Args:
        user_id (int): Идентификатор пользователя.
        movie_name (str): Название фильма.

    Returns:
        bool: True, если фильм успешно добавлен, 
        False в противном случае.
    """
    try:


    except Exception as exs:
        logger.error(
            f'Ошибка при добавлении фильма в избранное: {exc}'
        )
        return False
    ...
