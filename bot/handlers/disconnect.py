from telegram import Update
from telegram.error import TelegramError
from telegram.ext import CallbackContext
from mongo import chats

from .base import BaseCommand


class Disconnect(BaseCommand):
    OK_TEXT = (
        'You are disconnected\n'
        'Type /connect to start new conversation.'
    )

    FAIL_TEXT = (
        'You are not connected to any chat'
    )

    def _execute(self, user: dict, update: Update, context: CallbackContext) -> bool:
        chat = chats.get_chat(user['chat_id'])
        if not user:
            return False

        for chat_id in chat['users']:
            if chat_id != user['chat_id']:
                try:
                    context.bot.send_message(
                        chat_id=chat_id,
                        text=(
                            'Your partner has left the chat. Type /connect to start new conversation'
                        ),
                    )
                except TelegramError:
                    pass

        bool(chats.remove(chat['_id']))
        return True
