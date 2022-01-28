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
        response_json = response.json()
        try:
            object_from_json = Place.objects.get_or_create(
                title=response_json['title'],
                description_short=response_json['description_short'],
                description_long=response_json['description_long'],
                lng=float(response_json['coordinates']['lng']),
                lat=float(response_json['coordinates']['lat']),
            )[0]
            for uri in response_json['imgs']:
                file_name = split_file_name(uri)
                response = requests.get(uri)
                response.raise_for_status()
                image_from_json = Image()
                image_from_json.image.save(file_name, ContentFile(response.content), save=False)
                image_from_json.place = object_from_json
                image_from_json.save()
            print(object_from_json, object_from_json.id)
        except BaseException as error:
            print(f'Cant get json file from that way- {error}')
