from telegram import Update
from telegram.ext import CallbackContext

import settings

from mongo import users

from .base import BaseCommand


class Feedback(BaseCommand):
    HELP = (
        'написать разработчикам отзыв/вопрос/баг'
    )

    OK_TEXT = (
        'Сообщение получено. Спасибо.'
    )

    FAIL_TEXT = (
        'Пишите сообщение сразу, например "/feedback привет"'
    )

    def _execute(self, user: dict, update: Update, context: CallbackContext) -> bool:
        if not context.args:
            return False

        for admin in settings.TELEGRAM_ADMINS:
            context.bot.send_message(
                chat_id=admin,
                text='{} {}\n{}'.format(
                    users.get_user_str(user),
                    user['chat_id'],
                    ' '.join(context.args),
                ),
            )
        return True
