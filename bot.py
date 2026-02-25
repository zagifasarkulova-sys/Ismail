import logging
from telegram import (
    Update, WebAppInfo,
    InlineKeyboardButton, InlineKeyboardMarkup,
    MenuButtonWebApp, ReplyKeyboardMarkup, KeyboardButton
)
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

TOKEN = "8768072723:AAFnAKprrqCVFnyiaYanbBVR1Y7mzlkr3YY"
WEBAPP_URL = "https://zagifasarkulova-sys.github.io/Ismail/"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    name = user.first_name if user.first_name else "друг"

    keyboard = [
        [KeyboardButton(text="📱 Открыть приложение", web_app=WebAppInfo(url=WEBAPP_URL))]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        f"👋 Привет, {name}!\n\n"
        "🎓 Добро пожаловать в *English Learn* — твой личный репетитор английского!\n\n"
        "📚 Что тебя ждёт внутри:\n"
        "• 🗣 Словарный запас по темам\n"
        "• 📖 Грамматические правила\n"
        "• 🧪 Тесты и квизы\n"
        "• 🃏 Флэшкарты для запоминания слов\n"
        "• 📊 Твой прогресс и статистика\n\n"
        "👇 Нажми кнопку ниже чтобы начать!",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🆘 *Помощь*\n\n"
        "Доступные команды:\n"
        "/start — Запустить бота\n"
        "/help — Показать помощь\n"
        "/app — Открыть приложение\n\n"
        "📱 Нажми кнопку *«Открыть приложение»* в меню чтобы начать учиться!",
        parse_mode="Markdown"
    )


async def app_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton(
        text="📱 Открыть English Learn",
        web_app=WebAppInfo(url=WEBAPP_URL)
    )]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "👇 Нажми чтобы открыть приложение:",
        reply_markup=reply_markup
    )


async def setup_menu(application):
    await application.bot.set_chat_menu_button(
        menu_button=MenuButtonWebApp(
            text="📱 Учиться",
            web_app=WebAppInfo(url=WEBAPP_URL)
        )
    )


def main():
    app = Application.builder().token(TOKEN).post_init(setup_menu).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("app", app_cmd))
    print("✅ Бот запущен!")
    app.run_polling()


if __name__ == "__main__":
    main()
