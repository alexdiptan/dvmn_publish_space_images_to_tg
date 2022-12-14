import argparse
import logging
import os
import time
from pathlib import Path
from random import shuffle

import telegram
from dotenv import load_dotenv

import common_functions


def get_images_from_folder(images_path) -> list:
    files_in_path = []
    tree = os.walk(images_path)

    for path, directories, files in tree:
        for file in files:
            files_in_path.append(Path(path, file))

    return files_in_path


def publish_images(bot_instance, images: list, sleep_timer: int) -> None:
    for image in images:
        common_functions.upload_document_to_tg(bot_instance, telegram_channel_id, image)
        logging.info(f'Publishing images {image} done. Next image will published after {sleep_timer} hours. Sleep.')
        time.sleep(sleep_timer * 3600)


def main():
    image_files = get_images_from_folder(image_folder)
    connection_try_count = 0
    connection_wait_long = 30
    connection_wait_short = 5

    while True:
        try:
            logging.info(f'Start publishing images.')
            shuffle(image_files)
            publish_images(bot, image_files, args.publication_frequency)
            connection_try_count = 0
            logging.info(f'Publishing images done.')
        except telegram.error.NetworkError:
            logging.info(f'NetworkError. There is no internet connection.')
            connection_try_count += 1

        if connection_try_count == 1:
            logging.info(f'Something wrong with your internet connection. Sleep {connection_wait_short} sec.')
            time.sleep(connection_wait_short)
        elif connection_try_count == 2:
            logging.info(f'Something wrong with your internet connection. Sleep {connection_wait_long} sec.')
            time.sleep(connection_wait_long)


if __name__ == '__main__':
    load_dotenv()
    telegram_token = os.environ['TELEGRAM_TOKEN']
    telegram_channel_id = os.environ['TELEGRAM_CHANNEL_ID']
    image_folder = 'images'

    bot = telegram.Bot(token=telegram_token)

    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--image_path", help="Path to image which should be published to telegram.")
    parser.add_argument("-f", "--publication_frequency", default=4, type=int,
                        help="How often need to publish photo(in hours). Four(4) hours by default.")
    args = parser.parse_args()

    if args.image_path:
        common_functions.upload_document_to_tg(bot, telegram_channel_id, args.image_path)
    else:
        main()
