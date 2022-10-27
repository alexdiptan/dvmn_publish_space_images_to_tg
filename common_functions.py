import datetime
import os
from pathlib import Path
from urllib.parse import urlsplit

import requests


def date_normalize(image_date: str) -> datetime:
    normalized_date = datetime.datetime.strptime(image_date, "%Y%m%d%H%M%S")
    return normalized_date


def get_file_name_and_file_extension(file_url: str) -> tuple:
    link_parts = urlsplit(file_url)
    _, original_file_name = os.path.split(link_parts.path)
    _, file_extension = os.path.splitext(original_file_name)
    file_name = f'image_{int(datetime.datetime.now().timestamp())}{file_extension}'

    return file_name, file_extension


def save_image(img_url: str, image_path: str, payload: dict = {}) -> None:
    Path(image_path).mkdir(parents=True, exist_ok=True)
    image_name, _ = get_file_name_and_file_extension(img_url)
    image_path = Path.cwd() / image_path / image_name
    response = requests.get(img_url, params=payload)
    response.raise_for_status()

    with open(image_path, 'wb') as file:
        file.write(response.content)


def upload_document_to_tg(bot_instance, tg_chanel_id: str, document_path: str) -> None:
    with open(document_path, 'rb') as f:
        bot_instance.send_document(chat_id=tg_chanel_id, document=f)
