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

    for command in commands:
        dispatcher.add_handler(CommandHandler(str(command), command))

    dispatcher.add_handler(ChatMemberHandler(ChatMember()))
    dispatcher.add_handler(MessageHandler(~Filters.command, Forward()))

    logging.info('Starting bot')

    commands_help_text = '\n'.join([
        command.help_text
        for command in commands
        if command.help_text
    ])

    for admin_id in settings.TELEGRAM_ADMINS:
        updater.bot.send_message(
            chat_id=admin_id,
            text='\n{}'.format(commands_help_text)
        )

    updater.start_polling()
    updater.idle()
