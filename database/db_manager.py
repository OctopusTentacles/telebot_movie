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
    try:
        existing_user = UserRegistration.select().where(
            UserRegistration.user_id == user_id).first()
        
        if existing_user:
            return True

        new_user = UserRegistration.create(
            user_id = user_id,
            user_name = user_name,
            favorite_movies = '',
            registration_date = datetime.now()
        )
        return True
    

    except IntegrityError:
        # Если пользователь с таким user_id уже существует:
        return False
    except Exception as exc:
        # Обработка других исключений:
        print('Ошибка в базе данных', exc)
        return False    