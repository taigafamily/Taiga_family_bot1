from telegram import Update
from telegram.ext import ContextTypes

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я бот кальянной Тайга Family.\n"
        "Чтобы забронировать, напиши /booking"
    )

async def booking_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Здесь можно добавить логику бронирования
    await update.message.reply_text("Функция бронирования пока в разработке.")
