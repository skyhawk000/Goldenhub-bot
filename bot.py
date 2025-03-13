import random
import logging
import asyncio
import sys
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler
from config import TOKEN, CHAT_ID, MIN_INTERVAL, MAX_INTERVAL
from messages import generate_random_message
from telegram.error import TelegramError

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Initialize the bot
bot = Bot(token=TOKEN)

# Global variable to control message sending
task = None

async def send_messages():
    """Send messages at random intervals."""
    while True:
        try:
            message = generate_random_message()
            await bot.send_message(chat_id=CHAT_ID, text=message)
            logging.info(f"Sent message:\n{message}")
            await asyncio.sleep(random.randint(MIN_INTERVAL, MAX_INTERVAL))
        except TelegramError as e:
            logging.error(f"Telegram API error: {e}")
            await asyncio.sleep(5)
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            await asyncio.sleep(5)

async def start(update: Update, context):
    """Start sending messages when /start is received."""
    global task
    if task is None:
        task = asyncio.create_task(send_messages())
        await update.message.reply_text("Bot started!")
    else:
        await update.message.reply_text("Bot is already running!")

async def stop(update: Update, context):
    """Stop sending messages when /stop is received."""
    global task
    if task:
        task.cancel()
        task = None
        await update.message.reply_text("Bot stopped!")
    else:
        await update.message.reply_text("Bot is not running!")

def main():
    """Start the bot."""
    if sys.platform.startswith("win"):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("stop", stop))

    logging.info("Bot is running...")
    app.run_polling()
if __name__ == "__main__":
    main()