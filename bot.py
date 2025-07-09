import logging
import os
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_CHAT_ID = int(os.getenv("ADMIN_CHAT_ID"))

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

user_data = {}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("Забронировать", callback_data="book")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Добро пожаловать в Taiga Family! Нажмите кнопку ниже, чтобы забронировать столик.", reply_markup=reply_markup)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "book":
        user_data[query.from_user.id] = {}
        await query.message.reply_text("Введите ваше имя:")
        return

    if query.data.startswith("time_"):
        time = query.data.split("_")[1]
        user_data[query.from_user.id]["time"] = time

        data = user_data[query.from_user.id]
        name = data.get("name", "—")
        phone = data.get("phone", "—")

        await context.bot.send_message(
            chat_id=ADMIN_CHAT_ID,
            text=(
                f"🔔 Новая бронь!\n\n"
                f"👤 Имя: {name}\n"
                f"📞 Телефон: {phone}\n"
                f"⏰ Время: {time}"
            ),
        )

        await query.message.reply_text("Спасибо! Ваша бронь принята.")
        user_data.pop(query.from_user.id, None)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    if user_id in user_data:
        data = user_data[user_id]
        if "name" not in data:
            data["name"] = update.message.text
            await update.message.reply_text("Введите ваш номер телефона:")
        elif "phone" not in data:
            data["phone"] = update.message.text
            keyboard = [
                [
                    InlineKeyboardButton("18:00", callback_data="time_18:00"),
                    InlineKeyboardButton("20:00", callback_data="time_20:00"),
                    InlineKeyboardButton("22:00", callback_data="time_22:00"),
                ]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await update.message.reply_text("Выберите время брони:", reply_markup=reply_markup)


def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.add_handler(CommandHandler("help", start))
    app.add_handler(CommandHandler("booking", start))
    app.add_handler(CommandHandler("menu", start))
    app.add_handler(CommandHandler("reserve", start))
    app.add_handler(CommandHandler("book", start))
    app.add_handler(CommandHandler("admin", start))
    app.add_handler(CommandHandler("info", start))
    app.add_handler(CommandHandler("taiga", start))
    app.add_handler(CommandHandler("restart", start))
    app.add_handler(CommandHandler("open", start))
    app.add_handler(CommandHandler("hype", start))
    app.add_handler(CommandHandler("🔥", start))
    app.add_handler(CommandHandler("hi", start))
    app.add_handler(CommandHandler("hey", start))
    app.add_handler(CommandHandler("ok", start))
    app.add_handler(CommandHandler("helpme", start))
    app.add_handler(CommandHandler("good", start))
    app.add_handler(CommandHandler("go", start))
    app.add_handler(CommandHandler("menuplease", start))
    app.add_handler(CommandHandler("plz", start))
    app.add_handler(CommandHandler("pls", start))

    app.add_handler(CommandHandler("cancel", start))
    app.add_handler(CommandHandler("exit", start))
    app.add_handler(CommandHandler("clear", start))

    app.add_handler(CommandHandler("🦫", start))
    app.add_handler(CommandHandler("🔥🔥🔥", start))

    app.add_handler(CommandHandler("again", start))

    app.add_handler(CommandHandler("назад", start))

    app.add_handler(CommandHandler("helphelp", start))

    app.add_handler(CommandHandler("adminhelp", start))

    app.add_handler(CommandHandler("hellotaiga", start))

    app.add_handler(CommandHandler("family", start))

    app.add_handler(CommandHandler("oktaiga", start))

    app.add_handler(CommandHandler("работаем", start))

    app.add_handler(CommandHandler("welcome", start))

    app.add_handler(CommandHandler("welcometaiga", start))

    app.add_handler(CommandHandler("yo", start))

    app.add_handler(CommandHandler("call", start))

    app.add_handler(CommandHandler("hello", start))

    app.add_handler(CommandHandler("begin", start))

    app.add_handler(CommandHandler("tap", start))

    app.add_handler(CommandHandler("now", start))

    app.add_handler(CommandHandler("table", start))

    app.add_handler(CommandHandler("meet", start))

    app.add_handler(CommandHandler("bro", start))

    app.add_handler(CommandHandler("sos", start))

    app.add_handler(CommandHandler("taigacrew", start))

    app.add_handler(CommandHandler("push", start))

    app.add_handler(CommandHandler("таблица", start))

    app.add_handler(CommandHandler("ок", start))

    app.add_handler(CommandHandler("стол", start))

    app.add_handler(CommandHandler("зал", start))

    app.add_handler(CommandHandler("хочу", start))

    app.add_handler(CommandHandler("бронь", start))

    app.add_handler(CommandHandler("тайга", start))

    app.add_handler(CommandHandler("давай", start))

    app.add_handler(CommandHandler("погнали", start))

    app.add_handler(CommandHandler("погнали🔥", start))

    app.add_handler(CommandHandler("готово", start))

    app.add_handler(CommandHandler("начать", start))

    app.add_handler(CommandHandler("начнем", start))

    app.add_handler(CommandHandler("поехали", start))

    app.add_handler(CommandHandler("бро", start))

    app.add_handler(CommandHandler("семья", start))

    app.add_handler(CommandHandler("бот", start))

    app.add_handler(CommandHandler("чат", start))

    app.add_handler(CommandHandler("боттайга", start))

    app.add_handler(CommandHandler("боттайга🔥", start))

    app.add_handler(CommandHandler("поехали🔥", start))

    app.add_handler(CommandHandler("привет", start))

    app.add_handler(CommandHandler("👋", start))

    app.add_handler(CommandHandler("🔥🔥", start))

    app.add_handler(CommandHandler("letgo", start))

    app.add_handler(CommandHandler("taiga🔥", start))

    app.add_handler(CommandHandler("zapusk", start))

    app.add_handler(CommandHandler("vpered", start))

    app.add_handler(CommandHandler("запуск", start))

    app.add_handler(CommandHandler("вперед", start))

    app.add_handler(CommandHandler("давай🔥", start))

    app.add_handler(CommandHandler("начало", start))

    app.add_handler(CommandHandler("open🔥", start))

    app.add_handler(CommandHandler("вперёд", start))

    app.add_handler(CommandHandler("связаться", start))

    app.add_handler(CommandHandler("контакты", start))

    app.add_handler(CommandHandler("контакт", start))

    app.add_handler(CommandHandler("admin🔥", start))

    app.add_handler(CommandHandler("я", start))

    app.add_handler(CommandHandler("кнопка", start))

    app.add_handler(CommandHandler("кнопку", start))

    app.add_handler(CommandHandler("жми", start))

    app.add_handler(CommandHandler("жмак", start))

    app.add_handler(CommandHandler("нажми", start))

    app.add_handler(CommandHandler("забронировать", start))

    app.add_handler(CommandHandler("🛎️", start))

    app.add_handler(CommandHandler("таигабот", start))

    app.add_handler(CommandHandler("хочу🔥", start))

    app.add_handler(CommandHandler("таигасемья", start))

    app.add_handler(CommandHandler("место", start))

    app.add_handler(CommandHandler("место🔥", start))

    app.add_handler(CommandHandler("место🔥🔥", start))

    app.add_handler(CommandHandler("место🔥🔥🔥", start))
