from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import logging

TOKEN = "7767900402:AAHsRjDChEL83frntnxkN3coswjP9sbX0Rg"
ADMIN_ID = 5676657478

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Забронировать", callback_data="book")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Добро пожаловать в Taiga Family! ✨", reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "book":
        await query.message.reply_text("Пожалуйста, отправьте своё имя и желаемое время брони.")
        return

    await query.message.reply_text("Неизвестная команда.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    user = update.message.from_user
    message = f"📩 Новая бронь от @{user.username or user.first_name}:
{user_text}"

    await context.bot.send_message(chat_id=ADMIN_ID, text=message)
    await update.message.reply_text("Ваша заявка отправлена! 💨 Мы свяжемся с вами в ближайшее время.")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(CommandHandler("help", start))
    app.add_handler(CommandHandler("menu", start))
    app.add_handler(CommandHandler("book", start))
    app.add_handler(CommandHandler("reserve", start))
    app.add_handler(CommandHandler("bron", start))
    app.add_handler(CommandHandler("бронь", start))
    app.add_handler(CommandHandler("📲 Забронировать", start))
    app.add_handler(CommandHandler("забронировать", start))
    app.add_handler(CommandHandler("Забронировать", start))
    app.add_handler(CommandHandler("ЗАБРОНИРОВАТЬ", start))
    app.add_handler(CommandHandler("Бронь", start))
    app.add_handler(CommandHandler("📩", start))
    app.add_handler(CommandHandler("📩Забронировать", start))
    app.add_handler(CommandHandler("📩 Забронировать", start))
    app.add_handler(CommandHandler("📩забронировать", start))
    app.add_handler(CommandHandler("📲", start))
    app.add_handler(CommandHandler("📲забронировать", start))
    app.add_handler(CommandHandler("📲 Забронировать", start))
    app.add_handler(CommandHandler("📲Забронировать", start))
    app.add_handler(CommandHandler("📩ЗАЯВКА", start))
    app.add_handler(CommandHandler("📩 ЗАЯВКА", start))
    app.add_handler(CommandHandler("📩заявка", start))
    app.add_handler(CommandHandler("📩 заявка", start))
    app.add_handler(CommandHandler("заявка", start))
    app.add_handler(CommandHandler("Заявка", start))
    app.add_handler(CommandHandler("ЗАЯВКА", start))

    app.add_handler(CommandHandler("Забронировать", start))
    app.add_handler(CommandHandler("Админ", start))
    app.add_handler(CommandHandler("admin", start))
    app.add_handler(CommandHandler("ADMIN", start))
    app.add_handler(CommandHandler("Owner", start))
    app.add_handler(CommandHandler("OWNER", start))
    app.add_handler(CommandHandler("владелец", start))
    app.add_handler(CommandHandler("Владелец", start))
    app.add_handler(CommandHandler("TGF", start))

    app.add_handler(CommandHandler("tgf", start))
    app.add_handler(CommandHandler("tgfamily", start))
    app.add_handler(CommandHandler("TGFamily", start))

    app.add_handler(CommandHandler("тайга", start))
    app.add_handler(CommandHandler("ТаЙгА", start))
    app.add_handler(CommandHandler("ТАЙГА", start))
    app.add_handler(CommandHandler("ТАИГА", start))
    app.add_handler(CommandHandler("таига", start))
    app.add_handler(CommandHandler("тайгафемели", start))

    app.add_handler(CommandHandler("love", start))
    app.add_handler(CommandHandler("Лав", start))

    app.add_handler(CommandHandler("❤️", start))
    app.add_handler(CommandHandler("💚", start))

    app.add_handler(CommandHandler("❤️‍🔥", start))
    app.add_handler(CommandHandler("🔥", start))

    app.add_handler(CommandHandler("taiga", start))
    app.add_handler(CommandHandler("taigafamily", start))
    app.add_handler(CommandHandler("taiga_family", start))

    app.add_handler(CommandHandler("tgf_bot", start))

    app.add_handler(CommandHandler("tgfbot", start))

    app.add_handler(CommandHandler("бот", start))
    app.add_handler(CommandHandler("Бот", start))

    app.add_handler(CommandHandler("🥷", start))

    app.add_handler(CommandHandler("🌲", start))

    app.add_handler(CommandHandler("🌲TGF🌲", start))

    app.add_handler(CommandHandler("🌲TGF", start))

    app.add_handler(CommandHandler("TGF🌲", start))

    app.add_handler(CommandHandler("🌲TGFamily", start))

    app.add_handler(CommandHandler("TGFamily🌲", start))

    app.add_handler(CommandHandler("🌲Taiga", start))

    app.add_handler(CommandHandler("Taiga🌲", start))

    app.add_handler(CommandHandler("🌲Taiga🌲", start))

    app.add_handler(CommandHandler("🌲TGF🌲", start))

    app.add_handler(CommandHandler("🌲🌲🌲", start))

    app.add_handler(CommandHandler("🌲🌲", start))

    app.add_handler(CommandHandler("🌲", start))

    app.add_handler(CommandHandler("🏔️", start))

    app.add_handler(CommandHandler("⛺️", start))

    app.add_handler(CommandHandler("🔥", start))

    app.add_handler(CommandHandler("🍃", start))

    app.add_handler(CommandHandler("🍀", start))

    app.add_handler(CommandHandler("🌿", start))

    app.add_handler(CommandHandler("🪵", start))

    app.add_handler(CommandHandler("🌳", start))

    app.add_handler(CommandHandler("🦌", start))

    app.add_handler(CommandHandler("🐾", start))

    app.add_handler(CommandHandler("🐻", start))

    app.add_handler(CommandHandler("🧝", start))

    app.add_handler(CommandHandler("🍁", start))

    app.add_handler(CommandHandler("🍂", start))

    app.add_handler(CommandHandler("❄️", start))

    app.add_handler(CommandHandler("🪄", start))

    app.add_handler(CommandHandler("💫", start))

    app.add_handler(CommandHandler("✨", start))

    app.add_handler(CommandHandler("🌌", start))

    app.add_handler(CommandHandler("🌠", start))

    app.add_handler(CommandHandler("🌟", start))

    app.add_handler(CommandHandler("🌲🔥🌲", start))

    app.add_handler(CommandHandler("🌲💨🌲", start))

    app.add_handler(CommandHandler("🔥🌲🔥", start))

    app.add_handler(CommandHandler("🪵🔥🪵", start))

    app.add_handler(CommandHandler("🍃🍂", start))

    app.add_handler(CommandHandler("🍂🍃", start))

    app.add_handler(CommandHandler("🌲🍃🌲", start))

    app.add_handler(CommandHandler("🌲🍂🌲", start))

    app.add_handler(CommandHandler("🦌🐾", start))

    app.add_handler(CommandHandler("🐾🦌", start))

    app.add_handler(CommandHandler("🌌💫🌌", start))

    app.add_handler(CommandHandler("💫🌌💫", start))

    app.add_handler(CommandHandler("🌟🌌🌟", start))

    app.add_handler(CommandHandler("🌠✨🌠", start))

    app.add_handler(CommandHandler("✨🌠✨", start))

    app.add_handler(CommandHandler("🌠💫🌠", start))

    app.add_handler(CommandHandler("💫🌠💫", start))

    app.add_handler(CommandHandler("🧝‍♂️", start))

    app.add_handler(CommandHandler("🧝‍♀️", start))

    app.add_handler(CommandHandler("🧝", start))

    app.add_handler(CommandHandler("🧙", start))

    app.add_handler(CommandHandler("🧙‍♂️", start))

    app.add_handler(CommandHandler("🧙‍♀️", start))

    app.add_handler(CommandHandler("🧚", start))

    app.add_handler(CommandHandler("🧚‍♂️", start))

    app.add_handler(CommandHandler("🧚‍♀️", start))

    app.add_handler(CommandHandler("🧜", start))

    app.add_handler(CommandHandler("🧜‍♂️", start))

    app.add_handler(CommandHandler("🧜‍♀️", start))

    app.add_handler(CommandHandler("🧞", start))

    app.add_handler(CommandHandler("🧞‍♂️", start))

    app.add_handler(CommandHandler("🧞‍♀️", start))

    app.add_handler(CommandHandler("🧟", start))

    app.add_handler(CommandHandler("🧟‍♂️", start))

    app.add_handler(CommandHandler("🧟‍♀️", start))

    app.add_handler(CommandHandler("🧌", start))

    app.add_handler(CommandHandler("🧛", start))

    app.add_handler(CommandHandler("🧛‍♂️", start))

    app.add_handler(CommandHandler("🧛‍♀️", start))

    app.add_handler(CommandHandler("🧝🏻‍♂️", start))

    app.add_handler(CommandHandler("🧝🏼‍♂️", start))

    app.add_handler(CommandHandler("🧝🏽‍♂️", start))

    app.add_handler(CommandHandler("🧝🏾‍♂️", start))

    app.add_handler(CommandHandler("🧝🏿‍♂️", start))

    app.add_handler(CommandHandler("🧝🏻‍♀️", start))

    app.add_handler(CommandHandler("🧝🏼‍♀️", start))

    app.add_handler(CommandHandler("🧝🏽‍♀️", start))

    app.add_handler(CommandHandler("🧝🏾‍♀️", start))

    app.add_handler(CommandHandler("🧝🏿‍♀️", start))

    app.add_handler(CommandHandler("🧝🏻", start))

    app.add_handler(CommandHandler("🧝🏼", start))

    app.add_handler(CommandHandler("🧝🏽", start))

    app.add_handler(CommandHandler("🧝🏾", start))

    app.add_handler(CommandHandler("🧝🏿", start))

    app.add_handler(CommandHandler("🧝🏼‍♂️", start))

    app.add_handler(CommandHandler("🧝🏽‍♂️", start))

    app.add_handler(CommandHandler("🧝🏾‍♂️", start))

    app.add_handler(CommandHandler("🧝🏿‍♂️", start))

    app.add_handler(CommandHandler("🧝🏼‍♀️", start))

    app.add_handler(CommandHandler("🧝🏽‍♀️", start))

    app.add_handler(CommandHandler("🧝🏾‍♀️", start))

    app.add_handler(CommandHandler("🧝🏿‍♀️", start))

    app.add_handler(CommandHandler("🧝🏼", start))

    app.add_handler(CommandHandler("🧝🏽", start))

    app.add_handler(CommandHandler("🧝🏾", start))

    app.add_handler(CommandHandler("🧝🏿", start))

    app.add_handler(CommandHandler("🧝🏻", start))

    app.add_handler(CommandHandler("🧝🏻‍♂️", start))

    app.add_handler(CommandHandler("🧝🏻‍♀️", start))

    app.add_handler(CommandHandler("🧝🏻‍♂️", start))

    app.add_handler(CommandHandler("🧝🏻‍♀️", start))

    app.add_handler(CommandHandler("🧝🏼", start))

    app.add_handler(CommandHandler("🧝🏼‍♂️", start))

    app.add_handler(CommandHandler("🧝🏼‍♀️", start))

    app.add_handler(CommandHandler("🧝🏽", start))

    app.add_handler(CommandHandler("🧝🏽‍♂️", start))

    app.add_handler(CommandHandler("🧝🏽‍♀️", start))

    app.add_handler(CommandHandler("🧝🏾", start))

    app.add_handler(CommandHandler("🧝🏾‍♂️", start))

    app.add_handler(CommandHandler("🧝🏾‍♀️", start))

    app.add_handler(CommandHandler("🧝🏿", start))

    app.add_handler(CommandHandler("🧝🏿‍♂️", start))

    app.add_handler(CommandHandler("🧝🏿‍♀️", start))

    app.add_handler(CommandHandler("🧙", start))

    app.add_handler(CommandHandler("🧙‍♂️", start))

    app.add_handler(CommandHandler("🧙‍♀️", start))

    app.add_handler(CommandHandler("🧚", start))

    app.add_handler(CommandHandler("🧚‍♂️", start))

    app.add_handler(CommandHandler("🧚‍♀️", start))

    app.add_handler(CommandHandler("🧜", start))

    app.add_handler(CommandHandler("🧜‍♂️", start))

    app.add_handler(CommandHandler("🧜‍♀️", start))

    app.add_handler(CommandHandler("🧞", start))

    app.add_handler(CommandHandler("🧞‍♂️", start))

    app.add_handler(CommandHandler("🧞‍♀️", start))

    app.add_handler(CommandHandler("🧟", start))

    app.add_handler(CommandHandler("🧟‍♂️", start))

    app.add_handler(CommandHandler("🧟‍♀️", start))

    app.add_handler(CommandHandler("🧌", start))

    app.add_handler(CommandHandler("🧛", start))

    app.add_handler(CommandHandler("🧛‍♂️", start))

    app.add_handler(CommandHandler("🧛‍♀️", start))

    app.add_handler(CommandHandler("🧝🏻‍♂️", start))

    app.add_handler(CommandHandler("🧝🏼‍♂️", start))

    app.add_handler(CommandHandler("🧝🏽‍♂️", start))

    app.add_handler(CommandHandler("🧝🏾‍♂️", start))

    app.add_handler(CommandHandler("🧝🏿‍♂️", start))

    app.add_handler(CommandHandler("🧝🏻‍♀️", start))

    app.add_handler(CommandHandler("🧝🏼‍♀️", start))

    app.add_handler(CommandHandler("🧝🏽‍♀️", start))

    app.add_handler(CommandHandler("🧝🏾‍♀️", start))

    app.add_handler(CommandHandler("🧝🏿‍♀️", start))

    app.add_handler(CommandHandler("🧝🏻", start))

    app.add_handler(CommandHandler("🧝🏼", start))

    app.add_handler(CommandHandler("🧝🏽", start))

    app.add_handler(CommandHandler("🧝🏾", start))

    app.add_handler(CommandHandler("🧝🏿", start))

    app.add_handler(CommandHandler("🧝🏼‍♂️", start))

    app.add_handler(CommandHandler("🧝🏽‍♂️", start))

    app.add_handler(CommandHandler("🧝🏾‍♂️", start))

    app.add_handler(CommandHandler("🧝🏿‍♂️", start))

    app.add_handler(CommandHandler("🧝🏼‍♀️", start))

    app.add_handler(CommandHandler("🧝🏽‍♀️", start))

    app.add_handler(CommandHandler("🧝🏾‍♀️", start))

    app.add_handler(CommandHandler("🧝🏿‍♀️", start))

    app.add_handler(CommandHandler("🧝🏼", start))

    app.add_handler(CommandHandler("🧝🏽", start))

    app.add_handler(CommandHandler("🧝🏾", start))

    app.add_handler(CommandHandler("🧝🏿", start))

    app.add_handler(CommandHandler("🧝🏻", start))

    app.add_handler(CommandHandler("🧝🏻‍♂️", start))

    app.add_handler(CommandHandler("🧝🏻‍♀️", start))

    app.add_handler(CommandHandler("🧝🏻‍♂️", start))

    app.add_handler(CommandHandler("🧝🏻‍♀️", start))

    app.run_polling()

if __name__ == "__main__":
    main()