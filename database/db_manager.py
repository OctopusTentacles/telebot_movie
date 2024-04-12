


from models import UserRequest
from peewee import IntegrityError


def save_user_registration(user_id, user_name):
    try:
        existing_user = UserRequest.select().where(
            UserRequest.user_id == user_id
        ).first()
        if existing_user:
            return True

        new_user = UserRequest.create(
            user_id = user_id,
            user_name = user_name,
            category = 'registration'
        )
        return True
    

    except Exception:
        return False
    