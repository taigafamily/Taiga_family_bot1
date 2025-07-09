import logging
import os
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID")

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    keyboard = [[KeyboardButton("Забронировать")]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(f"Привет, {user.first_name}! Добро пожаловать в Тайга Family.", reply_markup=reply_markup)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == "Забронировать":
        user = update.effective_user
        booking_message = (
            f"🔔 Новая бронь!

"
            f"👤 Пользователь: @{user.username or user.first_name}
"
            f"🆔 ID: {user.id}
"
        )
        await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=booking_message)
        await update.message.reply_text("Бронь отправлена! Ожидайте подтверждения.")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()
