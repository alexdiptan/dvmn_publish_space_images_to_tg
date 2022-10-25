import datetime
import os
from pathlib import Path
from urllib.parse import unquote, urlsplit

import requests


def date_normalize(image_date: str) -> datetime:
    normalized_date = datetime.datetime.strptime(image_date, "%Y%m%d%H%M%S")
    return normalized_date


def get_file_name_and_file_extension(file_url: str) -> tuple:
    link_parts = urlsplit(file_url)
    file_name_from_parts = os.path.split(link_parts.path)[-1:]
    file_extension_unquote = unquote(file_name_from_parts[0])
    file_extension = ''.join(os.path.splitext(file_extension_unquote)[-1:])
    file_name = f'image_{int(datetime.datetime.now().timestamp())}{file_extension}'

    return file_name, file_extension


def save_image(img_url: str, image_path: str, payload: dict):
    original_image_name = get_file_name_and_file_extension(img_url)[0]
    image_path = Path.cwd() / image_path / original_image_name

    response = requests.get(img_url, params=payload)
    response.raise_for_status()

    with open(image_path, 'wb') as file:
        file.write(response.content)
