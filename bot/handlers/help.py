from telegram import Update, ForceReply
from telegram.ext import CallbackContext
from mongo import users

from .base import BaseCommand


class Help(BaseCommand):
    def _execute(self, user: dict, update: Update, context: CallbackContext) -> bool:
        return True
