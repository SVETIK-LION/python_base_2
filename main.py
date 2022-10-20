from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from bot_commands import *
from configurations import TOKEN


def main():
    updater = Updater(TOKEN)

    updater.dispatcher.add_handler(CommandHandler("start", start_command))
    updater.dispatcher.add_handler(CommandHandler("question", another_question))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, sphere_answer))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
