import argparse
import logging
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


def publish_images(bot_instance, images: list, sleep_timer: int = 4) -> None:
    for image in images:
        telegram_functions.upload_document(bot_instance, telegram_chanel_id, image)
        logging.info(f'Publishing images {image} done. Next image will published after {sleep_timer} hours. Sleep.')
        time.sleep(sleep_timer * 3600)


def main():
    Path(image_folder).mkdir(parents=True, exist_ok=True)
    image_files = get_images_from_folder(image_folder)

    while True:
        logging.info(f'Start publishing images')
        shuffle(image_files)
        if args.publication_frequency:
            publish_images(bot, image_files, int(args.publication_frequency))
        else:
            publish_images(bot, image_files)
        logging.info(f'Publishing images done')


if __name__ == '__main__':
    load_dotenv()
    apod_token = os.environ['APOD_API_KEY']
    telegram_token = os.environ['TELEGRAM_TOKEN']
    telegram_chanel_id = os.environ['TELEGRAM_CHANEL_ID']
    image_folder = 'images'

    bot = telegram.Bot(token=telegram_token)

    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--image_path", help="Path to image which should be published to telegram.")
    parser.add_argument("-f", "--publication_frequency", help="How often need to publish photo(in hours). "
                                                              "Four(4) hours by default.")
    args = parser.parse_args()

    if args.image_path:
        telegram_functions.upload_document(bot, telegram_chanel_id, args.image_path)
    else:
        main()
