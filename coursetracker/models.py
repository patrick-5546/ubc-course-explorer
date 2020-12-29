from django.db import models

# consider changing engines to be able to use JSONFields
class Course(models.Model):
    course_name = models.CharField(max_length=200, default='')
    average = models.CharField(max_length=200, default='0')
    five_year_average = models.CharField(max_length=200, default='0')
    standard_deviation = models.CharField(max_length=200, default='0')
    distributions = models.TextField(default='')
    professors = models.TextField(default='')
    prerequisites = models.TextField(default='')
    corequisites = models.TextField(default='')
    dependencies = models.TextField(default='')
    name = models.CharField(max_length=200, default='')
    number_of_credits = models.CharField(max_length=200, default='0')
    course_description = models.TextField(default='')
    prerequistes_description = models.TextField(default='')
    corequisites_description = models.TextField(default='')
    link = models.TextField(default='')

    def __str__(self):
        return self.course_name