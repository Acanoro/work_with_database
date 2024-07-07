import csv

from django.core.management.base import BaseCommand
from django.utils.text import slugify

from phones.models import Phone


class Command(BaseCommand):
    help = 'Импортирует телефоны из файла CSV.'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Путь к CSV-файлу, который необходимо импортировать.')

    def handle(self, *args, **options):
        csv_file = options['csv_file']

        with open(csv_file, 'r', encoding='utf-8') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone_data in phones:
            phone, created = Phone.objects.get_or_create(
                id=phone_data['id'],
                defaults={
                    'name': phone_data['name'],
                    'price': phone_data['price'],
                    'image': phone_data['image'],
                    'release_date': phone_data['release_date'],
                    'lte_exists': phone_data['lte_exists'] == 'True',
                    'slug': slugify(phone_data['name'])
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Телефон успешно создан. {phone.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Телефон {phone.name} уже существует'))
