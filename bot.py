import logging
from telegram import Update, BotCommand
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "7767900402:AAHsRjDChEL83frntnxkN3coswjP9sbX0Rg"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Привет! Я бот кальянной Тайга Family.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Напиши /start чтобы начать.")

async def book(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    message = (
        f"📩 Новая бронь от @{user.username or user.first_name}:\n"
        f"{' '.join(context.args)}"
    )
    # Здесь можно добавить отправку админам или запись в базу
    await update.message.reply_text("Спасибо за бронь! Мы скоро свяжемся.")

def main() -> None:
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("book", book))

    app.run_polling()

if __name__ == "__main__":
    main()
