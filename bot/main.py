import logging

from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ChatMemberHandler,
)

import settings

from .handlers import *


def start_bot():
    updater = Updater(settings.TELEGRAM_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', Start()))
    dispatcher.add_handler(CommandHandler('connect', Connect()))
    dispatcher.add_handler(CommandHandler('disconnect', Disconnect()))
    dispatcher.add_handler(CommandHandler('help', Help()))

    dispatcher.add_handler(CommandHandler('show_chats', ShowChats()))
    dispatcher.add_handler(CommandHandler('show_users', ShowUsers()))

    dispatcher.add_handler(ChatMemberHandler(ChatMember()))

    dispatcher.add_handler(MessageHandler(~Filters.command, Forward()))

    logging.info('Starting bot')
    for admin_id in settings.TELEGRAM_ADMINS:
        updater.bot.send_message(
            chat_id=admin_id,
            text='Starting...'
        )

    updater.start_polling()
    updater.idle()
