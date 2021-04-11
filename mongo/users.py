import random

from pymongo.errors import DuplicateKeyError
from telegram import User

from mongo.client import db


def get_all_users():
    return db.users.find({})


def get_user(chat_id):
    return db.users.find_one({
        'chat_id': chat_id,
    })


def get_random_user(exclude=None):
    exclude = exclude or []
    users = list(
        db.users.find({
            'chat_id': {'$not': {'$in': exclude}},
            'chat_with': None,
        }, {
            'chat_id': True,
        }))

    if users:
        user = random.choice(users)
        if user:
            return user['chat_id']


def save_user(user: User):
    try:
        db.users.save({
            'chat_id': user.id,
            'username': user.username or '',
            'first_name': user.first_name or '',
            'last_name': user.last_name or '',
            'language': user.language_code or 'en',
            'chat_with': None,
        })
    except DuplicateKeyError:
        pass


def connect(first, second):
    modified = 0
    modified += db.users.update_one({
        'chat_id': first,
        'chat_with': None,
    }, {
        '$set': {
            'chat_with': second,
        },
    }).modified

    modified += db.users.update_one({
        'chat_id': second,
        'chat_with': None,
    }, {
        '$set': {
            'chat_with': first,
        },
    }).modified

    if modified != 2:
        db.users.update({
            'chat_id': {'$in': [first, second]}
        }, {
            '$set': {
                'chat_with': None,
            }}
        )
        return False

    return True


def get_connected_user(chat_id):
    return db.users.find_one({
        'chat_with': chat_id,
    })
