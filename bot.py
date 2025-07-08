from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "7767900402:AAHsRjDChEL83frntnxkN3coswjP9sbX0Rg"  # <-- Поставь сюда свой настоящий токен

# Админский чат (где будут уведомления о брони)
ADMIN_CHAT_ID = -5676657478  # <-- замени на свой чат id

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Забронировать", callback_data="book")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Добро пожаловать! Вы можете сделать бронь:", reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == "book":
        user = query.from_user
        message = (
            f"📩 Новая бронь от @{user.username or user.first_name}.\n"
            f"ID пользователя: {user.id}"
        )
        await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=message)
        await query.edit_message_text("Спасибо! Ваша бронь отправлена администратору.")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    app.run_polling()

if __name__ == "__main__":
    main()
