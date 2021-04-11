from telegram import Update
from telegram.ext import CallbackContext
from mongo import users
from mongo import chats

from .base import BaseAdminCommand


class ShowUsers(BaseAdminCommand):
    def _execute(self, user: dict, update: Update, context: CallbackContext) -> bool:
        _users = [u['username'] for u in users.get_all_users()]

        update.message.reply_text(
            '\n'.join(_users) or 'No users'
        )
        return True
