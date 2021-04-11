from telegram import Update
from telegram.ext import CallbackContext

from mongo import chats

from .base import BaseCommand


class Forward(BaseCommand):

    FAIL_TEXT = (
        'Вы ни с кем не общаетесь\n'
        'Напишите /connect чтобы найти собеседника'
    )

    def _execute(self, user: dict, update: Update, context: CallbackContext) -> bool:
        chat = chats.get_chat(user['chat_id'])
        if not chat:
            return False

        for chat_id in chat['users']:
            if chat_id != user['chat_id']:
                context.bot.send_message(chat_id=chat_id, text=update.message.text)

        return True
