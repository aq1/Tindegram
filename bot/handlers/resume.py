from gettext import gettext as _

from telegram import Update
from telegram.ext import CallbackContext
from mongo import (
    chats,
    users,
)

from .base import BaseCommand


class Resume(BaseCommand):
    HELP = _(
        'вернуться в поиск, пользователи смогут к вам подключиться'
    )

    OK_TEXT = _(
        'Вы вернулись в поиск.\n'
        'Теперь пользователи смогут вас найти. Напишите /pause чтобы остановить поиск'
    )

    def _execute(self, user: users.User, update: Update, context: CallbackContext) -> bool:
        chats.delete_chats_for_user(user.chat_id)
        users.user_set_paused(user.chat_id, False)
        return True
