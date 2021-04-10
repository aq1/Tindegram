import random

from pymongo.errors import DuplicateKeyError
from telegram import User

from mongo.client import db


def get_chat(chat_id):
    return db.chats.find_one({
        'users': chat_id,
    })


def get_all_chats():
    return db.chats.find({})


def connect(first, second):
    db.chats.remove({
        'users': {'$in': [first, second]},
    })

    db.chats.insert_one({
        'users': [first, second],
    })


def disconnect(chat_id):
    return db.chats.remove({
        'users': chat_id,
    })['n']


def remove(_id):
    return db.chats.remove({
        '_id': _id,
    })
