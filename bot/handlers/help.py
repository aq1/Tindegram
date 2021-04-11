from telegram import Update
from telegram.ext import CallbackContext

from .base import BaseCommand


class Help(BaseCommand):
    def _execute(self, user: dict, update: Update, context: CallbackContext) -> bool:
        return True
