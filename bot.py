import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

def start(update, context):
    keyboard = [
        [InlineKeyboardButton("Join Channel 1", url="https://t.me/Channel1")],
        [InlineKeyboardButton("Join Channel 2", url="https://t.me/Channel2")],
        [InlineKeyboardButton("Join Channel 3", url="https://t.me/Channel3")],
        [InlineKeyboardButton("Join Channel 4", url="https://t.me/Channel4")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please Join All My Update Channels To Use Me!', reply_markup=reply_markup)

def main():
    updater = Updater(os.environ.get('BOT_TOKEN'))  # Remove use_context=True
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
