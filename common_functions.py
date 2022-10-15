import datetime
import os
from urllib.parse import unquote, urlsplit

import requests


def date_normalize(image_date: str) -> datetime:
    normalized_date = datetime.datetime.strptime(image_date, "%Y%m%d%H%M%S")
    return normalized_date


def get_file_name(file_url: str) -> tuple:
    link_parts = urlsplit(file_url)
    file_name_from_parts = os.path.split(link_parts.path)[-1:]
    file_name = ''.join(os.path.splitext(unquote(file_name_from_parts[0]))[0:])
    file_extension = ''.join(os.path.splitext(unquote(file_name_from_parts[0]))[-1:])

    return file_name, file_extension


def save_image(img_url: str, image_path: str):
    original_image_name = get_file_name(img_url)[0]
    filepath = f'{image_path}/{original_image_name}'

    response = requests.get(img_url)
    response.raise_for_status()

    with open(filepath, 'wb') as file:
        file.write(response.content)
