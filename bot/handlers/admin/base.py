from ..base import BaseHandler

from telegram import Update
from telegram.ext import CallbackContext

import settings


class BaseAdminHandler(BaseHandler):

    @property
    def help_text(self) -> str:
        return ''

    def __call__(self, update: Update, context: CallbackContext) -> None:
        if update.effective_user.id not in settings.TELEGRAM_ADMINS:
            return
        return super().__call__(update, context)
