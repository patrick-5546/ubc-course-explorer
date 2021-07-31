from django.db import models


class Course(models.Model):
    course_name = models.CharField(max_length=10, default='err')
    average = models.CharField(max_length=20, default='err')
    five_year_average = models.CharField(max_length=20, default='err')
    lowest_average = models.CharField(max_length=20, default='err')
    highest_average = models.CharField(max_length=20, default='err')
    standard_deviation = models.CharField(max_length=20, default='err')
    distribution = models.CharField(max_length=70, default='err')
    distribution_term = models.CharField(max_length=5, default='err')
    sub_name = models.CharField(max_length=200, default='err')
    number_of_credits = models.CharField(max_length=5, default='err')
    course_description = models.TextField(default='err')
    prerequistes_description = models.TextField(default='err')
    corequisites_description = models.TextField(default='err')
    course_link = models.CharField(max_length=200, default='err')
    sections_teaching_team = models.JSONField(default=dict)
    professor_ratings = models.JSONField(default=list)
    prerequisite_tree = models.JSONField(default=dict)

    def __str__(self):
        return self.course_name
