from telegram import Update
from telegram.ext import CallbackContext

from mongo import users

from .base import BaseCommand


class Help(BaseCommand):
    HELP = (
        'подсказка по командам'
    )

    OK_TEXT = (
        'Если вы не хотите чтобы к вам подключались пользователи, просто остановите бота.\n'
        'А когда захотите пообщаться снова, возобновите его.\n'
        'Доступные команды:\n'
        '/start - первая команда, бот добавляет вас в список пользователей и к вам могут подключиться\n'
        '/connect - начать новый разговор\n'
        '/disconnect - закончить активный разговор\n'
        '/pause - приостановить поиск собеседников\n'
        '\n'
        'Бот пересылает текст, видео, фото, стикеры, анимацию, аудио и видео сообщения'
    )

    def _execute(self, user: users.User, update: Update, context: CallbackContext) -> bool:
        return True
