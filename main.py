from dotenv import load_dotenv
import requests

from pathlib import Path
from urllib.parse import urlsplit, unquote
import os


def save_image(img_url: str, image_path: str):
    original_image_name = get_file_name(img_url)[0]
    filepath = f'{image_path}/{original_image_name}'

    response = requests.get(img_url)
    response.raise_for_status()

    with open(filepath, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch(launch_url: str) -> list:
    response = requests.get(launch_url)
    response.raise_for_status()
    launch_pictures = response.json()['links']['flickr']['original']

    return launch_pictures


def get_file_name(file_url: str) -> tuple:
    link_parts = urlsplit(file_url)
    file_name_from_parts = os.path.split(link_parts.path)[-1:]
    file_name = ''.join(os.path.splitext(unquote(file_name_from_parts[0]))[0:])
    file_extension = ''.join(os.path.splitext(unquote(file_name_from_parts[0]))[-1:])

    return file_name, file_extension


def fetch_apod_images(token: str, images_count: int = 10) -> list:
    params = {'api_key': token,
              'count': images_count
    }
    url = 'https://api.nasa.gov/planetary/apod'
    response = requests.get(url, params=params)
    response.raise_for_status()

    apod_images = [apod_dict['hdurl'] for apod_dict in response.json() if 'hdurl' in apod_dict]

    return apod_images


def main():
    load_dotenv()
    apod_token = os.environ['APOD_API_KEY']
    image_folder = 'images'
    Path(image_folder).mkdir(parents=True, exist_ok=True)

    spacex_launch_url = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'
    spacex_image_urls = fetch_spacex_last_launch(spacex_launch_url)
    for spacex_image_url in spacex_image_urls:
        save_image(spacex_image_url, image_folder)

    apod_image_urls = fetch_apod_images(apod_token)
    for apod_image_url in apod_image_urls:
        save_image(apod_image_url, image_folder)


if __name__ == '__main__':
    main()
