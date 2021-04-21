from gettext import gettext as _

from telegram import Update
from telegram.ext import CallbackContext

import settings

from mongo import users

from .base import BaseHandler


class Feedback(BaseHandler):
    HELP = _(
        'написать разработчикам отзыв/вопрос/баг'
    )

    OK_TEXT = _(
        'Сообщение получено. Спасибо.'
    )

    FAIL_TEXT = _(
        'Пишите сообщение сразу, например "/feedback привет"'
    )

    def _execute(self, user: users.User, update: Update, context: CallbackContext) -> bool:
        if not context.args:
            return False

        for admin in settings.TELEGRAM_ADMINS:
            context.bot.send_message(
                chat_id=admin,
                text='{} {}\n{}'.format(
                    str(user),
                    user.chat_id,
                    ' '.join(context.args),
                ),
            )
        return True
