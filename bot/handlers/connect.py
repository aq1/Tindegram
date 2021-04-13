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

        partner_chat_id = chats.connect(user['chat_id'])

        if partner_chat_id:
            context.bot.send_message(
                chat_id=partner_chat_id,
                text='К вам подключился новый собеседник',
            )
        return bool(partner_chat_id)
