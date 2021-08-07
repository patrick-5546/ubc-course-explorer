from django.db import models


class Course(models.Model):
    '''Example: fields for Course MATH 220
        - course_name: MATH 220
        - sub_name: Mathematical Proof
        - course_link:
            https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-course&dept=MATH&course=220

        - average: 64.41908125919794
        - five_year_average: 66.20500633728011
        - standard_deviation: 17.04839260344701
        - number_of_credits: 3
        - lowest_average: 51.86
        - highest_average: 77.61818182
        - profile_link: https://ubcgrades.com/statistics-by-course#UBCV-MATH-220

        - distribution: [67, 50, 53, 60, 80, 75, 80, 61, 85, 34, 20]
        - distribution_term: 2020W
        - distribution_link: https://ubcgrades.com/#UBCV-2020W-MATH-220-OVERALL

        - sections_teaching_team: dictionary, where the keys are the sections numbers, and values a list of professors
            who have taught that section, sorted by recency then alphabetically
        - professor_ratings: see _append_prof_rating() in coursetracker/migrations/load_courses.py

        - course_description: Sets and functions; induction; cardinality;  properties of the real numbers; sequences,
            series, and limits. Logic, structure, style, and clarity of proofs emphasized throughout. [3-0-0]
        - prerequisites_description: Either (a) a score of 64% or higher in one of MATH 101, MATH 103, MATH 105, SCIE
            001 or (b) one of MATH 121, MATH 200, MATH 217, MATH 226, MATH 253, MATH 254.
        - corequisites_description: N/A
        - prerequisite_tree: see _create_preq_tree() in coursetracker/migrations/load_courses.py
    '''
    course_name = models.CharField(max_length=10, default='err')
    sub_name = models.CharField(max_length=200, default='err')
    course_link = models.CharField(max_length=200, default='err')

    # Course Profile
    average = models.CharField(max_length=20, default='err')
    five_year_average = models.CharField(max_length=20, default='err')
    standard_deviation = models.CharField(max_length=20, default='err')
    number_of_credits = models.CharField(max_length=5, default='err')
    lowest_average = models.CharField(max_length=20, default='err')
    highest_average = models.CharField(max_length=20, default='err')
    profile_link = models.CharField(max_length=200, default='err')

    # Distribution Information
    distribution = models.CharField(max_length=70, default='err')
    distribution_term = models.CharField(max_length=5, default='err')
    distribution_link = models.CharField(max_length=200, default='err')

    # Professor Information
    sections_teaching_team = models.JSONField(default=dict)
    professor_ratings = models.JSONField(default=list)

    # Prerequisite Tree Information
    course_description = models.TextField(default='err')
    prerequistes_description = models.TextField(default='err')
    corequisites_description = models.TextField(default='err')
    prerequisite_tree = models.JSONField(default=dict)

    def __str__(self):
        return self.course_name
