

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.

def start(bot, update):
  update.message.reply_text(main_menu_message(),
                            reply_markup=main_menu_keyboard())

def main_menu(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=main_menu_message(),
                        reply_markup=main_menu_keyboard())

def first_menu(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=first_menu_message(),
                        reply_markup=first_menu_keyboard())

def second_menu(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=second_menu_message(),
                        reply_markup=second_menu_keyboard())

def third_menu(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=third_menu_message(),
                        reply_markup=third_menu_keyboard())

def four_menu(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=four_menu_message(),
                        reply_markup=four_menu_keyboard())

# and so on for every callback_data option
def first_submenu(bot, update):
  pass

def second_submenu(bot, update):
  pass

############################ Keyboards #########################################
def main_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Consultar Sensores', callback_data='m1')],
              [InlineKeyboardButton('Controlar Luces', callback_data='m2')],
              [InlineKeyboardButton('Controlar Cortinas', callback_data='m3')],
              [InlineKeyboardButton('Controlar Ventiladores', callback_data='m4')]]
  return InlineKeyboardMarkup(keyboard)

def first_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Submenu 1-1', callback_data='m1_1')],
              [InlineKeyboardButton('Submenu 1-2', callback_data='m1_2')],
              [InlineKeyboardButton('Main menu', callback_data='main')]]
  return InlineKeyboardMarkup(keyboard)

def second_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Submenu 2-1', callback_data='m2_1')],
              [InlineKeyboardButton('Submenu 2-2', callback_data='m2_2')],
              [InlineKeyboardButton('Main menu', callback_data='main')]]
  return InlineKeyboardMarkup(keyboard)

def third_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Submenu 3-1', callback_data='m3_1')],
              [InlineKeyboardButton('Submenu 3-2', callback_data='m3_2')],
              [InlineKeyboardButton('Main menu', callback_data='main')]]
  return InlineKeyboardMarkup(keyboard)

def four_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Submenu 4-1', callback_data='m4_1')],
              [InlineKeyboardButton('Submenu 2-2', callback_data='m4_2')],
              [InlineKeyboardButton('Main menu', callback_data='main')]]
  return InlineKeyboardMarkup(keyboard)

############################# Messages #########################################
def main_menu_message():
  return 'Choose the option in main menu:'

def first_menu_message():
  return 'Choose the submenu in first menu:'

def second_menu_message():
  return 'Choose the submenu in second menu:'

def third_menu_message():
  return 'Choose the submenu in third menu:'

def four_menu_message():
  return 'Choose the submenu in four menu:'

#def start(bot, update):
#    """Send a message when the command /start is issued."""
#    bot.send_message(chat_id=update.message.chat_id, text='Hi!')


def help(bot, update):
    """Send a message when the command /help is issued."""
    bot.send_message(chat_id=update.message.chat_id, text='Help!')


def echo(bot, update):
    """Echo the user message."""
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)


def error(bot, update):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', bot, update.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("818687469:AAGJvxRleb3T1cY1yIgT3AQFBAT15rQao9g")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    ############################# Handlers #########################################
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CallbackQueryHandler(main_menu, pattern='main'))
    dp.add_handler(CallbackQueryHandler(first_menu, pattern='m1'))
    dp.add_handler(CallbackQueryHandler(second_menu, pattern='m2'))
    dp.add_handler(CallbackQueryHandler(third_menu, pattern='m3'))
    dp.add_handler(CallbackQueryHandler(four_menu, pattern='m4'))
    dp.add_handler(CallbackQueryHandler(first_submenu, pattern='m1_1'))
    dp.add_handler(CallbackQueryHandler(second_submenu, pattern='m2_1'))

    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()