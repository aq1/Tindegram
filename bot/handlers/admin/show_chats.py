from telegram import Update
from telegram.ext import CallbackContext
from mongo import users
from mongo import chats

from .base import BaseAdminCommand


class ShowChats(BaseAdminCommand):
    def _execute(self, user: dict, update: Update, context: CallbackContext) -> bool:
        _chats = chats.get_all_chats()
        result = []
        for chat in _chats:
            _users = [
                users.get_user(chat_id)['username']
                for chat_id in chat['users']
            ]
            result.append(' and '.join(_users))

        update.message.reply_text(
            '\n'.join(result) or 'No chats'
        )
        return True
