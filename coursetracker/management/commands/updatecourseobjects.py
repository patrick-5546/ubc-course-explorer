from django.core.management.base import BaseCommand, CommandError
from coursetracker.models import Course
from coursetracker.views import create_course

class Command(BaseCommand):
    help = 'Refreshes the fields of all Course objects; use after modifying representation'


    def handle(self, *args, **options):
        self.stdout.write('Refreshing all Course objects')
        courseNames = [course.course_name for course in Course.objects.all()]
        Course.objects.all().delete()
        for course in courseNames:
            create_course(course)