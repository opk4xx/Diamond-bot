from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Configuration
BOT_TOKEN = "8254272510:AAHkVUVsI5rslCOTFCk7mWOcRjQSzeLRu_I"
UPI_ID = "opk4xx@ybl"
DIAMOND_AMOUNT = 199
PRICE = 29

def start(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    context.bot.send_message(
        chat_id=chat_id,
        text=f"👋 Welcome!\n\n💎 {DIAMOND_AMOUNT} Diamonds = ₹{PRICE}\n"
             f"Pay via UPI: {UPI_ID}\nSend screenshot after payment."
    )

def handle_message(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    text = update.message.text.lower()
    if "screenshot" in text or "payment" in text:
        context.bot.send_message(chat_id=chat_id,
                                 text="📷 Screenshot received!\n💎 Diamonds added ✅")
    else:
        context.bot.send_message(chat_id=chat_id,
                                 text="⚠️ Please send your payment screenshot after paying via UPI.")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
