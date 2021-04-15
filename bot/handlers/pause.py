from telegram import Update
from telegram.ext import CallbackContext
from mongo import users
from mongo import chats

from .base import BaseCommand


class Pause(BaseCommand):
    HELP = (
        'не участвовать в поиске, пользователи не будут к вам подключаться'
    )

    OK_TEXT = (
        'Вы вышли из чата.\n'
        'Участие в поиске приостановлено. Чтобы вернуться в поиск напишите /start'
    )

    def _execute(self, user: dict, update: Update, context: CallbackContext) -> bool:
        chats.delete_chats_for_user(user['chat_id'])
        users.user_set_paused(user['chat_id'], True)
        return True
