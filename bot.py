import random
import logging
import asyncio
from telegram import Bot
from config import TOKEN, CHAT_ID, MIN_INTERVAL, MAX_INTERVAL
from messages import generate_messages
from telegram.error import TelegramError

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Initialize the bot
bot = Bot(token=TOKEN)

async def send_message():
    """Send deposit and withdrawal messages to the group at random intervals."""
    while True:
        try:
            message = generate_messages()
            await bot.send_message(chat_id=CHAT_ID, text=message)

            # Log the message sent
            logging.info(f"Sent message:\n{message}")

            # Wait for a random interval between 10 and 15 seconds
            await asyncio.sleep(random.randint(MIN_INTERVAL, MAX_INTERVAL))
        
        except TelegramError as e:
            logging.error(f"Telegram API error: {e}")
            await asyncio.sleep(5)  # Wait before retrying

        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            await asyncio.sleep(5)

if __name__ == "__main__":
    asyncio.run(send_message())