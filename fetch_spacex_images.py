import argparse
from pathlib import Path

import requests
from dotenv import load_dotenv

import common_functions as com_func


def fetch_spacex_last_launch(image_folder: str, launch_id: str = 'latest') -> None:
    print(image_folder, launch_id)
    launch_url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(launch_url)
    response.raise_for_status()
    spacex_image_urls = response.json()['links']['flickr']['original']

    for spacex_image_url in spacex_image_urls:
        com_func.save_image(spacex_image_url, image_folder)


def main():
    load_dotenv()
    image_folder = 'images'
    Path(image_folder).mkdir(parents=True, exist_ok=True)

    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--launch_id", help="SpaceX launch id, if you have.")
    args = parser.parse_args()

    if args.launch_id:
        fetch_spacex_last_launch(image_folder, args.launch_id)
    else:
        fetch_spacex_last_launch(image_folder)


if __name__ == '__main__':
    main()
