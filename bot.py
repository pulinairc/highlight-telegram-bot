#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Telegram Highlight bot for matterbridge.
"""

import logging
import os
import re
from pprint import pprint
from telegram import ForceReply, Update
from telegram.ext.filters import Filters
from telegram.replykeyboardmarkup import ReplyKeyboardMarkup
from telegram.replykeyboardremove import ReplyKeyboardRemove
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.updater import Updater
from telegram.ext.dispatcher import Dispatcher
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.parsemode import ParseMode

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def dohighlight(update: Update, context: CallbackContext):

    original_message = update.message.text
    message_without_nick = re.sub( r'<([a-zA-Z\[\]\\`_\^\{\|\}][a-zA-Z0-9\[\]\\`_\^\{\|\}-]{1,31})> ', '', original_message )

    if any( re.findall( r'rolle', message_without_nick, re.IGNORECASE ) ):
      mapped_tg_nick = '@rollee'
    elif any( re.findall( r'Fanny', message_without_nick, re.IGNORECASE ) ):
      mapped_tg_nick = '@Fannynen'
    elif any( re.findall( r'convulvau', message_without_nick, re.IGNORECASE ) ):
      mapped_tg_nick = '@jhuusari'
    elif any( re.findall( r'Nasuu|Nanna', message_without_nick, re.IGNORECASE ) ):
      mapped_tg_nick = '@Nasuu'
    elif any( re.findall( r'Pekafu', message_without_nick, re.IGNORECASE ) ):
      mapped_tg_nick = '@Pekafu'
    elif any( re.findall( r'raikas', message_without_nick, re.IGNORECASE ) ):
      mapped_tg_nick = '@Raikasta'
    elif any( re.findall( r'maakari', message_without_nick, re.IGNORECASE ) ):
      mapped_tg_nick = '@maakarinen'
    elif any( re.findall( r'blizzer', message_without_nick, re.IGNORECASE ) ):
      mapped_tg_nick = '@Blitzzeri'
    else:
      return

    update.message.reply_text(
      text=
      "Ping {0}".format(mapped_tg_nick, update.message.text),
      disable_web_page_preview=False,
      parse_mode=ParseMode.HTML,
      reply_to_message_id=update.message.message_id
    )

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Piip piip, virhe, error, tilt! "%s" aiheutti virheen "%s"', update, context.error)

def main():
    """Start the bot."""
    updater = Updater(os.getenv('TOKEN'), use_context=True)
    updater.dispatcher.add_handler(MessageHandler(Filters.text, dohighlight))
    updater.dispatcher.add_error_handler(error)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
