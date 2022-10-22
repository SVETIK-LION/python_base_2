import logging

from telegram import ReplyKeyboardRemove, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext, CallbackQueryHandler,
)

# Включаем логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# токен бота
BOT_TOKEN = "5423907310:AAGImbekFyoo3x2RPcnTYeXQZIYq-QzVZo8"

# глобальные константы хранят состояние
(
    OP_BUTTON_STATE,      # 1 op - operation
    NUM_A_INPUT_STATE,
    REPLY_NUM_A_STATE,    # 2
    REPLY_NUM_B_STATE,
    REPLY_CALC_STATE,
    RESTART_STATE,
) = range(6)

data = {
    "num_a": 0,
    "num_b": 0,
    "op": "",
    "num_type": float
}


def start_command(update: Update, context: CallbackContext) -> int:
    # отобразить клавиатуру

    kb = [
        [InlineKeyboardButton("Операции с R числами", callback_data="real_nums")],
        [InlineKeyboardButton("Операции с C числами", callback_data="complex_nums")],
    ]

    # TODO: 2* (по желанию) заменить InlineKeyboardMarkup на ReplyKeyboardMarkup
    reply_markup = InlineKeyboardMarkup(kb)
    update.message.reply_text("Выберите действие", reply_markup=reply_markup)

    return OP_BUTTON_STATE


def ops_select(update: Update, context: CallbackContext) -> int:
    num_type_str = update.callback_query.data    # real_nums или complex_nums
    data["num_type"] = float if num_type_str == "real_nums" else complex

    kb = [
        [InlineKeyboardButton("a + b", callback_data="+")],
        [InlineKeyboardButton("a - b", callback_data="-")],
    ]

    # отобразим клавиатуру
    reply_markup = InlineKeyboardMarkup(kb)
    update.callback_query.message.edit_text("Выберите операцию:", reply_markup=reply_markup)

    return NUM_A_INPUT_STATE


def num_a_input(update: Update, context: CallbackContext) -> int:
    data["op"] = update.callback_query.data

    update.callback_query.message.edit_text("Введите число A:")
    return REPLY_NUM_A_STATE


def reply_num_a_input(update: Update, context: CallbackContext) -> int:
    data["num_a"] = update.message.text.replace(" ", "")

    update.message.reply_text("Введите число B:")
    return REPLY_NUM_B_STATE


def reply_num_b_input(update: Update, context: CallbackContext) -> int:
    data["num_b"] = update.message.text.replace(" ", "")

    result = get_result()

    update.message.reply_text(f"Результат вычисления: {result}")
    update.message.reply_text(f"Наберите /start для запуска")

    return RESTART_STATE


def get_result():
    result = 0
    num_a = data["num_type"](data["num_a"])
    num_b = data["num_type"](data["num_b"])

    if data["op"] == "+":
        result = num_a + num_b
    elif data["op"] == "-":
        result = num_a - num_b

    return result


def cancel_command(update: Update, context: CallbackContext) -> int:
    """Cancels and ends the conversation."""
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text(
        'Нажмите /start, чтобы сделать еще вычисление.', reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(BOT_TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start_command)],
        states={
            OP_BUTTON_STATE: [CallbackQueryHandler(ops_select)],
            NUM_A_INPUT_STATE: [CallbackQueryHandler(num_a_input)],
            REPLY_NUM_A_STATE: [MessageHandler(Filters.text, reply_num_a_input)],
            REPLY_NUM_B_STATE: [MessageHandler(Filters.text, reply_num_b_input)],
            RESTART_STATE: [CommandHandler('start', start_command)],
        },
        fallbacks=[CallbackQueryHandler('cancel', cancel_command)],
    )

    dispatcher.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
