from django.db import models

# consider changing engines to be able to use JSONFields


class Course(models.Model):
    course_name = models.CharField(max_length=200, default='')
    average = models.CharField(max_length=200, default='0')
    five_year_average = models.CharField(max_length=200, default='0')
    # Branch Additions
    lowest_average = models.CharField(max_length=200, default='0')
    highest_average = models.CharField(max_length=200, default='0')
    # End of Branch Additions
    standard_deviation = models.CharField(max_length=200, default='0')
    distribution = models.TextField(default='')  # for the graph
    distribution_term = models.CharField(max_length=200, default='0')
    corequisites = models.TextField(default='')
    dependencies = models.TextField(default='')
    sub_name = models.CharField(max_length=200, default='')
    number_of_credits = models.CharField(max_length=200, default='0')
    course_description = models.TextField(default='')
    prerequistes_description = models.TextField(default='')
    corequisites_description = models.TextField(default='')
    course_link = models.TextField(default='')

    def __str__(self):
        return self.course_name
