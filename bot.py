import os
import logging
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# Logging စနစ် (Error တွေကို Render logs မှာ ကြည့်လို့ရအောင်)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Environment Variables များယူခြင်း (Render Dashboard မှာ ထည့်ပေးရမှာပါ)
TOKEN = os.getenv("BOT_TOKEN")
MMQR_API_SECRET = os.getenv("MMQR_API_SECRET")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text="မင်္ဂလာပါ။ MMQR Bot မှ ကြိုဆိုပါတယ်။"
    )

# MMQR API ခေါ်မယ့် function ဥပမာ
async def get_qr(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # MMQR API ခေါ်ယူခြင်း logic ကို ဒီမှာ ထည့်ပါ
    # ဥပမာ - response = requests.post("MMQR_URL", headers={"Secret": MMQR_API_SECRET})
    await update.message.reply_text("QR Code ထုတ်ပေးနေပါပြီ...")

if __name__ == '__main__':
    if not TOKEN:
        print("Error: BOT_TOKEN not found!")
    else:
        application = ApplicationBuilder().token(TOKEN).build()
        
        start_handler = CommandHandler('start', start)
        qr_handler = CommandHandler('qr', get_qr)
        
        application.add_handler(start_handler)
        application.add_handler(qr_handler)
        
        # Polling စနစ်နဲ့ run ခြင်း (Render အတွက် အဆင်ပြေဆုံး)
        application.run_polling()
      
