from gettext import gettext as _

from telegram import Update
from telegram.ext import CallbackContext
from mongo import users

from .base import BaseHandler


class Start(BaseHandler):
    HELP = _(
        'бот добавляет вас в список пользователей, но не добавляет в поиск'
    )

    OK_TEXT = _(
        'Привет. Этот бот создает чат со случайным пользователем.\n'
        'Мы не храним ваши сообщения.\n'
        'Но все равно относитесь отвественно к тому что отправляете\n'
        'Нажмите /connect чтобы начать первый разговор. '
        'Напишите /pause чтобы временно убрать себя из поиска.\n'
        'Пересылаются текст, фото, видео, стикеры, анимация, голосовые и видео сообщения'
    )

    def _execute(self, user: users.User, update: Update, context: CallbackContext) -> bool:
        return True
