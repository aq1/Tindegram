from telegram import Update, Message, Bot, TelegramError
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
                try:
                    self._forward_message(
                        bot=context.bot,
                        chat_id=chat_id,
                        message=update.message
                    )
                except TelegramError:
                    update.message.reply_text(
                        text=(
                            'Не удалось переслать сообщение. '
                            'Возможно пользователь приостановил бота.'
                        )
                    )

        return True

    @staticmethod
    def _forward_message(bot: Bot, chat_id: int, message: Message) -> None:
        if message.sticker:
            bot.send_sticker(chat_id=chat_id, sticker=message.sticker)
        elif message.voice:
            bot.send_voice(chat_id=chat_id, voice=message.voice)
        elif message.video_note:
            bot.send_video_note(chat_id=chat_id, video_note=message.video_note)
        elif message.animation:
            bot.send_animation(chat_id=chat_id, animation=message.animation)
        elif message.photo:
            bot.send_photo(chat_id=chat_id, photo=message.photo[0])
        elif message.video:
            bot.send_video(chat_id=chat_id, video=message.video)
        elif message.text:
            bot.send_message(chat_id=chat_id, text=message.text)
        else:
            bot.send_message(
                chat_id=message.chat_id,
                text='Пересылка таких сообщений пока не поддерживается',
            )
