import os

import telegram
from dotenv import load_dotenv


def upload_document(bot_instance, tg_chanel_id: str, document_path: str):
    with open(document_path, 'rb') as f:
        bot_instance.send_document(chat_id=tg_chanel_id, document=f)


def send_message(bot_instance, tg_chanel_id: str, message: str) -> None:
    bot_instance.send_message(chat_id=tg_chanel_id, text=message)


if __name__ == '__main__':
    load_dotenv()
    telegram_token = os.environ['TELEGRAM_TOKEN']
    telegram_chanel_id = os.environ['TELEGRAM_CHANEL_ID']
    bot = telegram.Bot(token=telegram_token)
    upload_document(bot, telegram_chanel_id, 'images/jan8_sxt_big.gif')
