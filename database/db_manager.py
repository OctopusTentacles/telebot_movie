""" Модуль проверки регистрации пользователей. """


from datetime import datetime
from .models import UserRegistration
from peewee import IntegrityError


def save_user_registration(user_id: int, user_name: str) -> bool:
    """Сохраняет регистрацию пользователя в базе данных.

    Args:
        user_id (int): Идентификатор пользователя.
        user_name (str): Имя пользователя.

    Returns:
        bool: True, если регистрация прошла успешно,
              False в противном случае.
    """
    existing_user = UserRegistration.select().where(
        UserRegistration.user_id == user_id).first()
    
    if existing_user:
        print('Пользователь уже существует в базе данных')
        return True

    try:
        new_user = UserRegistration.create(
            user_id=user_id,
            user_name=user_name,
            favorite_movies='',
            registration_date=datetime.now()
        )
        print('Пользователь успешно зарегистрирован')
        return True

    except IntegrityError:
        print('Ошибка регистрации: пользователь уже существует')
        return False

    except Exception as exc:
        print('Ошибка в базе данных:', exc)
        return False
    