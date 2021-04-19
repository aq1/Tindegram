from typing import Any, List

from pymongo.errors import DuplicateKeyError
from telegram import User as TelegramUser

from mongo.client import db


class User:
    def __init__(self, user_dict: dict[str, Any]):
        self.chat_id: int = user_dict['chat_id']
        self.username: str = user_dict['username']
        self.first_name: str = user_dict['first_name']
        self.last_name: str = user_dict['last_name']
        self.language: str = user_dict['language']
        self.paused: bool = user_dict['paused']

    def __str__(self) -> str:
        return str(self.username or f'{self.first_name} {self.last_name}')


def get_all_users() -> List[User]:
    return [User(u) for u in db.users.find({}).sort('paused')]


def get_user(chat_id: int) -> User:
    return User(db.users.find_one({
        'chat_id': chat_id,
    }))


def save_user(user: TelegramUser) -> User:
    user_dict = {
        'chat_id': user.id,
        'username': user.username or '',
        'first_name': user.first_name or '',
        'last_name': user.last_name or '',
        'language': user.language_code or 'en',
        'chat_with': None,
        'paused': True,
    }
    try:
        db.users.update(
            {'chat_id': user.id},
            user_dict,
            upsert=True,
        )
    except DuplicateKeyError:
        pass

    return User(user_dict)


def delete_user(chat_id: int) -> None:
    db.users.remove({
        'chat_id': chat_id,
    })


def user_set_paused(chat_id: int, value: bool) -> None:
    db.users.update_one({
        'chat_id': chat_id,
    }, {
        '$set': {
            'paused': value,
        }
    })
