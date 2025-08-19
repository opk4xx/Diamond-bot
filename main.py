from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# ---- Yaha apna bot token daalo ----
BOT_TOKEN = "8254272510:AAHkVUVsI5rslCOTFCk7mWOcRjQSzeLRu_I"

# ---- Apna UPI ID ----
UPI_ID = "opk4xx@ybl"

# /start command
def start(update, context):
    text = (
        "👋 Welcome to Free Fire Diamond Generator Bot!\n\n"
        "💎 199 Diamonds = ₹29 only\n\n"
        "📌 Pay via UPI:\n"
        f"👉 {UPI_ID}\n\n"
        "Payment ke baad screenshot bheje, fir diamonds aapke ID pe send kar diye jayenge ✅"
    )
    update.message.reply_text(text)

# Agar koi message bheje to
def handle_message(update, context):
    update.message.reply_text("⚡ Payment ke baad apna Free Fire ID aur screenshot bheje!")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
