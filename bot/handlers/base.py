import logging

import sentry_sdk
from telegram import Update
from telegram.ext import CallbackContext
import stringcase

from mongo import users


class BaseCommand:
    HELP = ''
    OK_TEXT = ''
    FAIL_TEXT = ''

    @property
    def help_text(self) -> str:
        return f'{self} - {self.HELP}'

    def _execute(self, user: dict, update: Update, context: CallbackContext) -> bool:
        return NotImplemented

    def __call__(self, update: Update, context: CallbackContext) -> None:
        user = users.get_user(update.effective_user.id)

        if user:
            sentry_sdk.set_context('user', {
                'username': user['username'],
                'chat_id': user['chat_id'],
            })

        try:
            ok = self._execute(user, update, context)
        except Exception as e:
            logging.exception(str(e))
            update.message.reply_text(
                'Произошла ошибка. '
                'Бот находится в разработке, так что это неудивительно',
            )
            return

        text = [self.FAIL_TEXT, self.OK_TEXT][ok]

        if text:
            update.effective_chat.send_message(text)

    def __str__(self):
        return stringcase.snakecase(self.__class__.__name__)
