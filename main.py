import os
import time
from pathlib import Path
from random import shuffle

import telegram
from dotenv import load_dotenv

import fetch_apod_images
import fetch_epic_images
import fetch_spacex_images
import telegram_functions


def get_images_from_folder(images_path) -> list:
    files_in_path = []
    tree = os.walk(images_path)

    for path, directories, files in tree:
        for file in files:
            files_in_path.append(os.path.join(f'{path}/{file}'))

    return files_in_path


def publish_images(bot_instance, images: list, sleep_timer: int) -> None:
    for image in images:
        telegram_functions.upload_document(bot_instance, telegram_chanel_id, image)
        time.sleep(sleep_timer * 3600)


def main():
    Path(image_folder).mkdir(parents=True, exist_ok=True)
    image_files = get_images_from_folder(image_folder)
    bot = telegram.Bot(token=telegram_token)

    while True:
        if len(image_files) == 0:
            fetch_apod_images.fetch_apod_images(image_folder, apod_token)
            fetch_epic_images.fetch_epic_images('https://api.nasa.gov/EPIC/api/natural?api_key=DEMO_KEY')
            fetch_spacex_images.fetch_spacex_launch_images(image_folder, '5eb87d47ffd86e000604b38a')
        else:
            publish_images(bot, image_files, int(publication_frequency))
            shuffle(image_files)
            publish_images(bot, image_files, int(publication_frequency))


if __name__ == '__main__':
    load_dotenv()
    apod_token = os.environ['APOD_API_KEY']
    image_folder = os.environ['IMAGES_FOLDER']
    telegram_token = os.environ['TELEGRAM_TOKEN']
    telegram_chanel_id = os.environ['TELEGRAM_CHANEL_ID']
    publication_frequency = os.environ['PUBLICATION_FREQUENCY']

    main()
