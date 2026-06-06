import os
import logging
import threading
import requests
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# --- ၁။ Flask Web Server (Render Port အတွက်) ---
app = Flask('')

@app.route('/')
def home():
    return "Bot is alive and running!"

def run_flask():
    # Render က ပေးတဲ့ PORT ကို ယူသုံးခြင်း (Default 8080)
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = threading.Thread(target=run_flask)
    t.start()

# --- ၂။ Telegram Bot Logic ---
# Logging စနစ် (Render logs မှာ ကြည့်လို့ရအောင်)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Environment Variables များယူခြင်း
TOKEN = os.getenv("BOT_TOKEN")
MMQR_API_SECRET = os.getenv("MMQR_API_SECRET")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("မင်္ဂလာပါ။ MMQR Bot မှ ကြိုဆိုပါတယ်။")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("အကူအညီအတွက် /start ကို နှိပ်ပါ။")

# --- ၃။ Main Execution ---
if __name__ == '__main__':
    # Web server ကို background မှာ စတင်နှိုးခြင်း
    keep_alive()
    
    if not TOKEN:
        logging.error("Error: BOT_TOKEN is missing in environment variables!")
    else:
        # Bot Application ကို တည်ဆောက်ခြင်း
        application = ApplicationBuilder().token(TOKEN).build()
        
        # Handlers များ ထည့်သွင်းခြင်း
        application.add_handler(CommandHandler('start', start))
        application.add_handler(CommandHandler('help', help_command))
        
        logging.info("Bot started. Listening for messages...")
        
        # Polling စနစ်ဖြင့် Bot ကို စတင် run ခြင်း
        application.run_polling()

