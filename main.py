import Responses as r
from telegram.ext import *
import CONSTANTS as keys

print("Starting bot...")

def start_command(update, context):
    """
    Start command
    """
    update.message.reply_text(r.welcome())

def help_command(update, context):
    """
    Help command
    """
    update.message.reply_text(r.help())

def handle_message(update, context):
    """
    Handle message
    """
    update.message.reply_text(r.handle_response(update.message.text))

def main():
    """
    Main function
    """
    updater = Updater(keys.BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start_command))
    dispatcher.add_handler(CommandHandler('help', help_command))
    dispatcher.add_handler(MessageHandler(Filters.text, handle_message))
    updater.start_polling()


main()
