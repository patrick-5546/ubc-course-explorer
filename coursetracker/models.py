from django.db import models


class Course(models.Model):
    course_name = models.CharField(max_length=10, default='err')
    average = models.CharField(max_length=20, default='err')
    five_year_average = models.CharField(max_length=20, default='err')
    lowest_average = models.CharField(max_length=20, default='err')
    highest_average = models.CharField(max_length=20, default='err')
    standard_deviation = models.CharField(max_length=20, default='err')
    distribution = models.TextField(default='err')
    distribution_term = models.CharField(max_length=5, default='err')
    corequisites = models.TextField(default='err')
    dependencies = models.TextField(default='err')
    sub_name = models.CharField(max_length=100, default='err')
    number_of_credits = models.CharField(max_length=5, default='err')
    course_description = models.TextField(default='err')
    prerequistes_description = models.TextField(default='err')
    corequisites_description = models.TextField(default='err')
    course_link = models.TextField(default='err')

    def __str__(self):
        return self.course_name
