import logging
from telegram import Update, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup, MenuButtonWebApp
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

TOKEN = r”8768072723:AAFnAKprrqCVFnyiaYanbBVR1Y7mzlkr3YY”
WEBAPP_URL = r”https://zagifasarkulova-sys.github.io/Ismail/”

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
keyboard = [[InlineKeyboardButton(text=r”Open IELTS Master”, web_app=WebAppInfo(url=WEBAPP_URL))]]
reply_markup = InlineKeyboardMarkup(keyboard)
await update.message.reply_text(text=r”Welcome to IELTS Master! Press the button below to start!”, reply_markup=reply_markup)

async def setup_menu(application):
await application.bot.set_chat_menu_button(menu_button=MenuButtonWebApp(text=r”IELTS App”, web_app=WebAppInfo(url=WEBAPP_URL)))

def main():
app = Application.builder().token(TOKEN).post_init(setup_menu).build()
app.add_handler(CommandHandler(r”start”, start))
print(r”Bot started!”)
app.run_polling()

if **name** == r”**main**”:
main()
