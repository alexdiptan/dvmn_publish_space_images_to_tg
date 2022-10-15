import os

import telegram
from dotenv import load_dotenv


def upload_document(bot_instance, tg_chanel_id: str, document_path: str):
    bot_instance.send_document(chat_id=tg_chanel_id, document=open(document_path, 'rb'))


def send_message(bot_instance, tg_chanel_id: str, message: str) -> None:
    bot_instance.send_message(chat_id=tg_chanel_id, text=message)


if __name__ == '__main__':
    load_dotenv()
    telegram_token = os.environ['TELEGRAM_TOKEN']
    telegram_chanel_id = os.environ['TELEGRAM_CHANEL_ID']
    bot = telegram.Bot(token=telegram_token)
