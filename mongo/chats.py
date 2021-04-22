from typing import Optional

from mongo.client import db


def get_chat(chat_id) -> dict:
    return db.chats.find_one({
        'users': chat_id,
    })


def get_all_chats():
    return db.chats.find({})


def connect(chat_id: int) -> Optional[int]:
    try:
        busy_users = db.chats.aggregate([
            {'$unwind': '$users'},
            {'$group': {'_id': None, '_users': {'$addToSet': '$users'}}},
            {'$project': {'_id': 0, 'users': '$_users'}}
        ]).next()['users']
    except (StopIteration, KeyError):
        busy_users = []

    try:
        partner_chat_id = db.users.aggregate([
            {'$match': {
                'chat_id': {'$not': {'$in': busy_users}, '$ne': chat_id},
                'paused': False,
            }},
            {'$sample': {'size': 1}}
        ]).next()['chat_id']
    except (StopIteration, KeyError):
        return False

    db.chats.remove({
        'users': {'$in': [chat_id, partner_chat_id]},
    })

    db.chats.insert_one({
        'users': [chat_id, partner_chat_id],
    })

    return partner_chat_id


def disconnect(chat_id):
    return db.chats.remove({
        'users': chat_id,
    })['n']


def delete_chats_for_user(chat_id: int) -> None:
    db.chats.remove({
        'users': chat_id,
    })
