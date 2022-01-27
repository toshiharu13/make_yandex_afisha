from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'load dump utility'

    def add_arguments(self, parser):
        parser.add_argument(
            'way_to',
            type=str,
            help='Введите путь к файлу'
        )

    def handle(self, *args, **options):
        print(options["way_to"])
