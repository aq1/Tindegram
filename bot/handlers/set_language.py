from gettext import gettext as _

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from telegram.ext import CallbackContext

from mongo import users

from .base import BaseHandler


class SetLanguage(BaseHandler):
    HELP = _(
        'установить язык интерфейса'
    )

    def _execute(self, user: users.User, update: Update, context: CallbackContext) -> bool:
        keyboard = [[
            InlineKeyboardButton('Русский', callback_data='ru'),
            InlineKeyboardButton('English', callback_data='en'),
        ]]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text(_('Выберите язык:'), reply_markup=reply_markup)
        return True


class SetLanguageQuery(BaseHandler):
    def _execute(self, user: users.User, update: Update, context: CallbackContext) -> bool:
        query = update.callback_query
        query.answer()
        users.set_language(user.chat_id, query.data)
        query.edit_message_text(text=_('Язык выбран: {}').format(query.data))
        return True
