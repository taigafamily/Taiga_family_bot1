import logging
import os
from dotenv import load_dotenv
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    ApplicationBuilder,
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    filters,
)

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
admin_id_env = os.getenv("ADMIN_ID")
if admin_id_env is None:
    raise ValueError("Environment variable ADMIN_ID is not set!")
ADMIN_ID = int(admin_id_env)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

NAME, PHONE, TIME = range(3)

def start(update: Update, context: CallbackContext):
    keyboard = [[InlineKeyboardButton("📅 Забронировать стол", callback_data="book")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Добро пожаловать в кальянную Taiga Family!", reply_markup=reply_markup)

def start_booking(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.message.reply_text("Введите ваше имя:")
    return NAME

def get_name(update: Update, context: CallbackContext):
    context.user_data["name"] = update.message.text
    update.message.reply_text("Введите ваш номер телефона:")
    return PHONE

def get_phone(update: Update, context: CallbackContext):
    context.user_data["phone"] = update.message.text
    update.message.reply_text("На какое время хотите сделать бронь?")
    return TIME

def get_time(update: Update, context: CallbackContext):
    context.user_data["time"] = update.message.text
    name = context.user_data["name"]
    phone = context.user_data["phone"]
    time = context.user_data["time"]

    text = (
        f"🔔 Новая бронь!\n\n"
        f"👤 Имя: {name}\n"
        f"📞 Телефон: {phone}\n"
        f"🕒 Время: {time}"
    )

    context.bot.send_message(chat_id=ADMIN_ID, text=text)
    update.message.reply_text("Ваша бронь принята! Ждём вас 🤍")
    return ConversationHandler.END

def cancel(update: Update, context: CallbackContext):
    update.message.reply_text("Бронирование отменено.")
    return ConversationHandler.END

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CallbackQueryHandler(start_booking, pattern="^book$")],
        states={
            NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_name)],
            PHONE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_phone)],
            TIME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_time)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    app.add_handler(CommandHandler("start", start))
    app.add_handler(conv_handler)

    app.run_polling()

if __name__ == "__main__":
    main()
