from telegram import Update
from telegram.constants import CHATMEMBER_KICKED
from telegram.ext import CallbackContext

from mongo import (
    users,
    chats,
)
from .base import BaseCommand


class ChatMember(BaseCommand):
    def _execute(self, user: dict, update: Update, context: CallbackContext) -> bool:
        if update.my_chat_member.new_chat_member.status == CHATMEMBER_KICKED:
            users.delete_user(user['chat_id'])
            chats.delete_chats_for_user(user['chat_id'])

        return True
