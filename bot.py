import os
import logging
from telegram import Update, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup, MenuButtonWebApp
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(**name**)

TOKEN = ‘8447477957:AAHAEm48qRPkQJcWf8cn7XrZejYFuHoO-z0’
WEBAPP_URL = ‘https://zagifasarkulova-sys.github.io/Ismail/’

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
keyboard = [[InlineKeyboardButton(‘Open IELTS Master’, web_app=WebAppInfo(url=WEBAPP_URL))]]
reply_markup = InlineKeyboardMarkup(keyboard)
await update.message.reply_text(‘Welcome to IELTS Master! Press the button below to start!’, reply_markup=reply_markup)

async def setup_menu(application):
await application.bot.set_chat_menu_button(menu_button=MenuButtonWebApp(text=‘IELTS App’, web_app=WebAppInfo(url=WEBAPP_URL)))

def main():
app = Application.builder().token(TOKEN).post_init(setup_menu).build()
app.add_handler(CommandHandler(‘start’, start))
print(‘Bot started!’)
app.run_polling()

if **name** == ‘**main**’:
main()
