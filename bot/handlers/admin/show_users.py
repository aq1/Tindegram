from telegram import Update
from telegram.ext import CallbackContext
from mongo import users
from mongo import chats

from .base import BaseAdminHandler


class ShowUsers(BaseAdminHandler):
    def _execute(self, user: users.User, update: Update, context: CallbackContext) -> bool:
        _users = [
            '{} {} {}'.format(
                '⏹' if u.paused else '👌',
                u.language,
                str(u),
            )
            for u in users.get_all_users()
        ]

        update.message.reply_text(
            '\n'.join(_users) or 'No users'
        )
        return True
