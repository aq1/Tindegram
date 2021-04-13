from telegram import Update
from telegram.ext import CallbackContext
from mongo import users

from .base import BaseCommand


class Start(BaseCommand):
    OK_TEXT = (
        'Привет. Этот бот создает чат со случайным пользователем.\n'
        'Мы не храним ваши сообщения.\n'
        'Нажмите /connect чтобы начать первый разговор. '
        'Пересылаются текст, фото, видео, стикеры, анимация, голосовые и видео сообщения'
    )

    def _execute(self, user: dict, update: Update, context: CallbackContext) -> bool:
        users.save_user(update.effective_user)
        return True
