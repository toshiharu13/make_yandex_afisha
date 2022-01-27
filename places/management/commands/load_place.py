import requests
from django.core.management.base import BaseCommand, CommandError

from places.models import Place


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
        print(response_json)
        try:
            #print(options['way_to'])
            object_from_json = Place.objects.get_or_create(
                title=response_json['title'],
                description_short=response_json['description_short'],
                description_long=response_json['description_long'],
                lng=float(response_json['coordinates']['lng']),
                lat=float(response_json['coordinates']['lat']),
            )
            print(object_from_json)
        except BaseException as error:
            print(f'Cant get json file from that way- {error}')
