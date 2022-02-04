import os
from pathlib import Path
from urllib.parse import urlparse

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand, CommandError
from django.shortcuts import get_object_or_404

from places.models import Image, Place
from where_to_go.settings import MEDIA_ROOT


def split_file_name(url):
    """
    Функция парсинга имени файла из ссылки
    :param url: ссылка на скачивание
    :return: имя файла
    """
    parse_url = urlparse(url)
    path_to_file = parse_url.path
    file_name = os.path.split(path_to_file)[1]
    return file_name


class Command(BaseCommand):
    help = 'load dump utility'

    def add_arguments(self, parser):
        parser.add_argument(
            'way_to',
            type=str,
            help='Введите путь к файлу'
        )

    def handle(self, *args, **options):
        response = requests.get(options["way_to"])
        response.raise_for_status()
        place_raw = response.json()
        try:
            object_from_link, object_status = Place.objects.get_or_create(
                title=place_raw['title'],
                description_short=place_raw['description_short'],
                description_long=place_raw['description_long'],
                lng=float(place_raw['coordinates']['lng']),
                lat=float(place_raw['coordinates']['lat']),
            )
            for uri in place_raw['imgs']:
                file_name = split_file_name(uri)
                response = requests.get(uri)
                response.raise_for_status()

                image_from_link = Image()
                image_from_link.image.save(
                    file_name, ContentFile(response.content), save=False)
                image_from_link.place = object_from_link
                image_from_link.save()
            print(object_from_link, object_from_link.id)
        except BaseException as error:
            print(f'Cant get json file from that way- {error}')
