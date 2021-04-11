import logging

from telegram import Update
from telegram.ext import CallbackContext

from mongo import users


class BaseCommand:
    OK_TEXT = ''
    FAIL_TEXT = ''

    def _execute(self, user: dict, update: Update, context: CallbackContext) -> bool:
        return NotImplemented

    def __call__(self, update: Update, context: CallbackContext) -> None:
        user = users.get_user(update.effective_user.id)
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
