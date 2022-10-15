import os

import telegram
from dotenv import load_dotenv


def send_message(tg_token: str, tg_chanel_id: str, message: str) -> None:
    bot = telegram.Bot(token=tg_token)
    bot.send_message(chat_id=tg_chanel_id, text=message)


if __name__ == '__main__':
    load_dotenv()
    telegram_token = os.environ['TELEGRAM_TOKEN']
    telegram_chanel_id = os.environ['TELEGRAM_CHANEL_ID']

    send_message(telegram_token, telegram_chanel_id, 'Test message here.')
