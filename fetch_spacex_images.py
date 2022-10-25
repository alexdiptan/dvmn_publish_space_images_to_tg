import argparse
from pathlib import Path

import requests
from dotenv import load_dotenv

import common_functions as com_func


def fetch_spacex_launch_images(image_folder: str, launch_id: str) -> None:
    launch_url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(launch_url)
    response.raise_for_status()
    spacex_image_urls = response.json()['links']['flickr']['original']
    payload = {}

    for spacex_image_url in spacex_image_urls:
        com_func.save_image(spacex_image_url, image_folder, payload)


def main():
    load_dotenv()
    image_folder = 'images'
    Path(image_folder).mkdir(parents=True, exist_ok=True)
    token = 'DEMO_KEY'

    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--launch_id", default='latest', help="SpaceX launch id, if you have.")
    args = parser.parse_args()
    fetch_spacex_launch_images(image_folder, args.launch_id)


if __name__ == '__main__':
    main()
