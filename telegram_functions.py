import os

import telegram
from dotenv import load_dotenv


load_dotenv()
telegram_token = os.environ['TELEGRAM_TOKEN']
telegram_chanel_id = os.environ['TELEGRAM_CHANEL_ID']

bot = telegram.Bot(token=telegram_token)
updates = bot.get_updates()
print(bot.get_me())
# print(updates[2])

bot.send_message(chat_id=telegram_chanel_id, text="Test message here.")
