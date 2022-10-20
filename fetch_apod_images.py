import argparse
import os
from pathlib import Path

import requests
from dotenv import load_dotenv

import common_functions as com_func


def fetch_apod_images(image_folder: str, token: str, images_count: int) -> None:
    params = {'api_key': token,
              'count': images_count
              }
    url = 'https://api.nasa.gov/planetary/apod'
    response = requests.get(url, params=params)
    response.raise_for_status()

    apod_image_urls = [apod_dict['hdurl'] for apod_dict in response.json() if 'hdurl' in apod_dict]

    for apod_image_url in apod_image_urls:
        com_func.save_image(apod_image_url, image_folder)


def main():
    load_dotenv()
    apod_token = os.environ['APOD_API_KEY']
    image_folder = 'images'
    Path(image_folder).mkdir(parents=True, exist_ok=True)

    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--count_to_save", default=5, help="Files count to save.")
    args = parser.parse_args()

    fetch_apod_images(image_folder, apod_token, args.count_to_save)


if __name__ == '__main__':
    main()
