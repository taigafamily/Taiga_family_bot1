import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

TOKEN = os.getenv("TOKEN")
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID")

bookings = {}

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["Забронировать"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Добро пожаловать в кальянную Taiga Family! Нажмите кнопку ниже, чтобы забронировать столик.", reply_markup=reply_markup)

# Обработка кнопки "Забронировать"
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    user_id = update.effective_user.id

    if text == "Забронировать":
        await update.message.reply_text("Пожалуйста, введите ваше имя и время брони (например: Алексей, 20:00).")
        bookings[user_id] = {}
    elif user_id in bookings and not bookings[user_id]:
        bookings[user_id] = text
        msg = f"📌 Новая бронь:\n👤 {update.effective_user.full_name}\n📝 {text}"
        await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=msg)
        await update.message.reply_text("Спасибо! Ваша бронь отправлена.")
    else:
        await update.message.reply_text("Нажмите «Забронировать», чтобы начать бронирование.")

# Запуск бота
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()
