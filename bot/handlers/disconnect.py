from gettext import gettext as _

from telegram import Update
from telegram.error import TelegramError
from telegram.ext import CallbackContext
from mongo import (
    chats,
    users,
)

from .base import BaseHandler


class Disconnect(BaseHandler):
    HELP = _(
        'закончить активный разговор'
    )

    OK_TEXT = _(
        'Вы закончили разговор\n'
        'Напишите /connect чтобы начать новый'
    )

    FAIL_TEXT = _(
        'Вы ни с кем не общаетесь'
    )

    def _execute(self, user: users.User, update: Update, context: CallbackContext) -> bool:
        chat = chats.get_chat(user.chat_id)
        if not chat:
            return False

        for chat_id in chat['users']:
            if chat_id != user.chat_id:
                try:
                    context.bot.send_message(
                        chat_id=chat_id,
                        text=_(
                            'Ваш собеседник покинул чат. Напишите /connect чтобы найти нового'
                        ),
                    )
                except TelegramError:
                    pass

        bool(chats.disconnect(user.chat_id))
        return True
