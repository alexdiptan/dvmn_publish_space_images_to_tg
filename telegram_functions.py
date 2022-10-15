import os

import telegram
from dotenv import load_dotenv


def upload_document(tg_chanel_id: str, document_path: str):
    bot.send_document(chat_id=tg_chanel_id, document=open(document_path, 'rb'))


def send_message(tg_chanel_id: str, message: str) -> None:
    bot.send_message(chat_id=tg_chanel_id, text=message)


if __name__ == '__main__':
    load_dotenv()
    telegram_token = os.environ['TELEGRAM_TOKEN']
    telegram_chanel_id = os.environ['TELEGRAM_CHANEL_ID']
    bot = telegram.Bot(token=telegram_token)

    upload_document(telegram_chanel_id, 'images/gliese876_dss_1.gif')
    # send_message(telegram_token, telegram_chanel_id, 'Test message here.')
