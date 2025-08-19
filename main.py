from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# ---- Yaha apna Token aur UPI ID daalna ----
TOKEN = "8254272510:AAHkVUVsI5rslCOTFCk7mWOcRjQSzeLRu_I"
UPI_ID = "opk4xx@ybl"

# ---- Commands ----
def start(update, context):
    update.message.reply_text(
        f"👋 Welcome to Diamond Generator Bot!\n\n"
        f"💎 199 Diamonds = ₹29 only\n\n"
        f"📌 Pay on UPI: {UPI_ID}\n\n"
        f"✅ After payment send screenshot here."
    )

def help_cmd(update, context):
    update.message.reply_text(
        "❓ Help:\n\n"
        "1. Type /start to see diamond details.\n"
        "2. Pay ₹29 on given UPI ID.\n"
        "3. Send screenshot here.\n"
        "4. Verification ke baad diamonds milega ✅"
    )

def handle_photo(update, context):
    update.message.reply_text("📷 Screenshot received! Verification ke baad diamonds milega ✅")

def handle_text(update, context):
    update.message.reply_text("⚠️ Sirf screenshot bhejo ya /start likho!")

# ---- Bot Setup ----
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_cmd))
    dp.add_handler(MessageHandler(Filters.photo, handle_photo))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
