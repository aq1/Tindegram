from telegram import Update, ForceReply
from telegram.ext import CallbackContext
from mongo import users

from .base import BaseCommand


class Start(BaseCommand):
    OK_TEXT = (
        'Hello. This bot creates chat with a random user.\n'
        'We do not store your messages.\n'
        'Type /connect to start your first conversation.'
    )

    def _execute(self, user: dict, update: Update, context: CallbackContext) -> bool:
        users.save_user(update.effective_user)
        return True
