from telegram import Update
from telegram.ext import CallbackContext
from mongo import users
from mongo import chats

from .base import BaseCommand


class Connect(BaseCommand):
    OK_TEXT = (
        'You are connected! Start chatting.\n'
        'Type /disconnect to stop the conversation.'
    )

    FAIL_TEXT = (
        'Could not connect with a user.\n'
        'They are all busy probably.'
    )

    def _execute(self, user: dict, update: Update, context: CallbackContext) -> bool:
        random_chat_id = users.get_random_user(exclude=[user['chat_id']])
        if not random_chat_id:
            return False

        chats.connect(user['chat_id'], random_chat_id)
        return True
