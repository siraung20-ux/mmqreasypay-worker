import os
import telebot
from flask import Flask
from threading import Thread

# ၁။ Bot Token နဲ့ MMQR Secret ကို Environment Variable ကနေယူမယ်
TOKEN = os.environ.get('BOT_TOKEN')
MMQR_SECRET = os.environ.get('MMQR_API_SECRET')

bot = telebot.TeleBot(TOKEN)
app = Flask('')

# ၂။ Render က Port စစ်တဲ့အခါ အောင်မြင်အောင် လုပ်ပေးတဲ့အပိုင်း
@app.route('/')
def home():
    return "Bot is running!"

def run_web_server():
    # Render ကပေးတဲ့ PORT ကို ယူသုံးမယ်၊ မရှိရင် ၈၀၈၀ သုံးမယ်
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

# ၃။ Bot Command များ
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "မင်္ဂလာပါ။ MMQR Bot အလုပ်လုပ်နေပါပြီ။")

@bot.message_handler(commands=['check'])
def check_status(message):
    bot.reply_to(message, "Bot Status: Online ✅")

# ၄။ Web Server နဲ့ Bot ကို တစ်ပြိုင်တည်း run ဖို့ function
def start_bot():
    print("Bot is starting...")
    bot.infinity_polling()

if __name__ == "__main__":
    # Web server ကို thread တစ်ခုနဲ့ background မှာ နှိုးထားမယ်
    t = Thread(target=run_web_server)
    t.start()
    
    # Bot ကို main thread မှာ run မယ်
    start_bot()
    
