import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    CallbackQueryHandler,
    MessageHandler,
    filters,
)
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Забронировать", callback_data="book_now")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Добро пожаловать в Taiga Family! 🌲", reply_markup=reply_markup)

# Обработка кнопки "Забронировать"
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("Введите, пожалуйста, ваше имя:")

    context.user_data["booking_stage"] = "name"

# Обработка последовательного ввода бронирования
async def booking_input_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    stage = context.user_data.get("booking_stage")

    if stage == "name":
        context.user_data["name"] = text
        context.user_data["booking_stage"] = "date"
        await update.message.reply_text("Введите дату брони (например, 2025-07-10):")
    elif stage == "date":
        context.user_data["date"] = text
        context.user_data["booking_stage"] = "time"
        await update.message.reply_text("Введите время брони (например, 20:00):")
    elif stage == "time":
        context.user_data["time"] = text
        context.user_data["booking_stage"] = None

        name = context.user_data.get("name")
        date = context.user_data.get("date")
        time = context.user_data.get("time")

        admin_chat_id = os.getenv("ADMIN_CHAT_ID")
        booking_msg = (
            f"Новая бронь:\n\n👤 Имя: {name}\n📅 Дата: {date}\n⏰ Время: {time}\n🆔 Telegram ID: {update.effective_user.id}"
        )

        await update.message.reply_text("Спасибо! Ваша бронь принята. ✅")
        if admin_chat_id:
            await context.bot.send_message(chat_id=admin_chat_id, text=booking_msg)

# Главная точка входа
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), booking_input_handler))

    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
