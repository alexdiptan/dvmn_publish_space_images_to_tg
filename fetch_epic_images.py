import os
from pathlib import Path

import requests
from dotenv import load_dotenv

import common_functions as com_func


def fetch_epic_images(url: str, api_token: str) -> list:
    payload = {'api_key': api_token}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    epic_images = []

    for image in response.json():
        current_image_date = com_func.date_normalize(image["identifier"])
        epic_images.append(f'https://api.nasa.gov/EPIC/archive/natural/{current_image_date.year}/'
                           f'{current_image_date.month}/{current_image_date.day}/png/'
                           f'{image["image"]}.png')

    return epic_images


def main():
    load_dotenv()
    token = os.getenv('NASA_API_KEY', default='DEMO_KEY')
    image_folder = 'images'
    Path(image_folder).mkdir(parents=True, exist_ok=True)
    payload = {'api_key': token}

    epic_image_urls = fetch_epic_images('https://api.nasa.gov/EPIC/api/natural', token)
    for epic_image_url in epic_image_urls:
        com_func.save_image(epic_image_url, image_folder, payload)


if __name__ == '__main__':
    main()
