from telegram import Update
from telegram.ext import CallbackContext
from mongo import users
from mongo import chats

from .base import BaseAdminHandler


class ShowUsers(BaseAdminHandler):
    def _execute(self, user: users.User, update: Update, context: CallbackContext) -> bool:
        users_in_chats = chats.get_users_in_chats()

        _users = []

        for user in users.get_all_users():
            status = 'π'
            if user.chat_id in users_in_chats:
                status = 'π¬'
            elif user.paused:
                status = 'βΉ'

            language = 'πΊπΈ'
            if user.language == 'ru':
                language = 'π·πΊ'

            _users.append('{}{}{}'.format(
                status,
                language,
                str(user)
            ))

        update.message.reply_text(
            '\n'.join(_users) or 'No users'
        )

        return True
