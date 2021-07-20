from django.core.management.base import BaseCommand  # , CommandError
from coursetracker.models import Course
from coursetracker.views import create_course


class Command(BaseCommand):
    help = 'Refreshes the fields of all Course objects; use after modifying representation'

    def handle(self, *args, **options):
        courseNames = [course.course_name for course in Course.objects.all()]
        Course.objects.all().delete()
        for course in courseNames:
            code = course.split(' ')
            create_course(code[0], code[1])
        self.stdout.write('Successfully refreshed all Course objects')
