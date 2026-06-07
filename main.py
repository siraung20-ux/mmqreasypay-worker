from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💸 MMQR Easy Pay\n\n"
        "Minimum: 500 MMK\n"
        "Maximum: 1,000,000 MMK\n\n"
        "ငွေပမာဏ ရိုက်ထည့်ပါ။"
    )

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
