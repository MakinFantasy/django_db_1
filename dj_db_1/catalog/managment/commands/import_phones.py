import csv

from django.template.defaultfilters import slugify
from dj_db_1.catalog.models import Phone
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open("phones.csv") as csvfile:
            reader = csv.reader(csvfile, delimeter=';')
            next(reader)
            for item in reader:
                phone = Phone.objects.create(
                    id=int(item[0]), name=item[1],
                    image=item[2], price=item[3],
                    realese_date=item[4], lte_exists=item[5],
                    slug=slugify(item[1]),
                )
