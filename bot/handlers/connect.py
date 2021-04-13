from telegram import Update
from telegram.ext import CallbackContext
from mongo import users
from mongo import chats

from .base import BaseCommand


class Connect(BaseCommand):
    OK_TEXT = (
        'Собеседник найден! Начинайте общение.\n'
        'Напишите /disconnect чтобы остановить разговор.'
    )

    FAIL_TEXT = (
        'Пользователь не найден.\n'
        'Скорее всего они заняты в других чатах.'
    )

    def _execute(self, user: dict, update: Update, context: CallbackContext) -> bool:
        if user['paused']:
            users.user_set_paused(user['chat_id'], False)
        try:
            exclude = chats.get_chat(user['chat_id'])['users']
        except TypeError:
            exclude = [user['chat_id']]

        random_chat_id = users.get_random_user(exclude=exclude)
        if not random_chat_id:
            return False

        chats.connect(user['chat_id'], random_chat_id)
        context.bot.send_message(
            chat_id=random_chat_id,
            text='К вам подключился новый собеседник',
        )
        return True
