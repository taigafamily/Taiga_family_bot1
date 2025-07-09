import logging
import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

user_data = {}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("Забронировать", callback_data="book")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Привет! Я бот кальянной Тайга Family 🍃", reply_markup=reply_markup)


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "book":
        await query.message.reply_text("Введите имя:")
        user_data[query.from_user.id] = {"step": "name"}


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    text = update.message.text

    if user_id in user_data:
        step = user_data[user_id].get("step")

        if step == "name":
            user_data[user_id]["name"] = text
            user_data[user_id]["step"] = "date"
            await update.message.reply_text("Введите дату и время брони (например, 12 июля 20:00):")

        elif step == "date":
            user_data[user_id]["date"] = text
            name = user_data[user_id]["name"]
            date = user_data[user_id]["date"]

            await update.message.reply_text("Спасибо! Ваша бронь принята ✅")

            # Отправка админу
            if ADMIN_CHAT_ID:
                await context.bot.send_message(
                    chat_id=int(ADMIN_CHAT_ID),
                    text=f"🔔 Новая бронь!\n\n👤 Имя: {name}\n📅 Дата и время: {date}\n🆔 Telegram: @{update.message.from_user.username or 'Без username'}"
                )
            user_data.pop(user_id)


def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))
    app.run_polling()


if __name__ == "__main__":
    main()
