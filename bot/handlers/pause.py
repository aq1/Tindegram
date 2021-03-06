from gettext import gettext as _

from telegram import Update
from telegram.ext import CallbackContext
from mongo import (
    chats,
    users,
)

from .base import BaseHandler


class Pause(BaseHandler):
    HELP = _(
        'не участвовать в поиске, пользователи не будут к вам подключаться'
    )

    OK_TEXT = _(
        'Вы вышли из чата.\n'
        'Участие в поиске приостановлено. Чтобы вернуться в поиск напишите /resume'
    )

    def _execute(self, user: users.User, update: Update, context: CallbackContext) -> bool:
        chats.delete_chats_for_user(user.chat_id)
        users.user_set_paused(user.chat_id, True)
        return True
