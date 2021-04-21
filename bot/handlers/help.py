from gettext import gettext as _

from telegram import Update
from telegram.ext import CallbackContext

from mongo import users

from .base import BaseHandler


class Help(BaseHandler):
    HELP = _(
        'подсказка по командам'
    )

    OK_TEXT = _(
        'Доступные команды:\n'
        '/start - первая команда, бот добавляет вас в список пользователей\n'
        '/connect - начать новый разговор\n'
        '/disconnect - закончить активный разговор\n'
        '/feedback {сообщение} - отправить сообщение разработчикам\n'
        '/pause - приостановить поиск собеседников\n'
        '/resume - вернуться в поиск, пользователи смогут вас найти'
        '\n'
        'Бот пересылает текст, видео, фото, стикеры, анимацию, аудио и видео сообщения'
    )

    def _execute(self, user: users.User, update: Update, context: CallbackContext) -> bool:
        return True
