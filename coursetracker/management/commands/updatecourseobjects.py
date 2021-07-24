from django.core.management.base import BaseCommand  # , CommandError
from coursetracker.models import Course

from coursetracker.migrations.load_courses import load_courses


class Command(BaseCommand):
    help = 'Refreshes the fields of all Course objects; use after modifying representation'

    def handle(self, *args, **options):
        Course.objects.all().delete()
        print('Deleted all Course objects')
        load_courses(Course)
        print('Finished refreshing all Course objects')
