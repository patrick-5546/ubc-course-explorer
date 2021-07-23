# Generated by Django 3.1.13 on 2021-07-21 23:32

import json
import os

from django.db import IntegrityError, migrations, transaction

from .ubc_course_explorer_data.scripts.update_data import (
    AVAILABLE_COURSES_FN, COURSE_INFORMATION_FN, COURSE_STATISTICS_FN, GRADE_DISTRIBUTIONS_FN
)

Course = None  # Course model
DATA_DIR_PATH = os.path.join(os.path.join('coursetracker', 'migrations'), 'ubc_course_explorer_data')

# Data from files
AVAIL_COURSES = None
COURSE_INFO = None
COURSE_STATS = None
GRADE_DISTRS = None
# create these files in new repo
# once this is working, figure out prerequisite tree and ubc grades + rmp profs info


def load_courses(apps, schema_editor):
    '''Saves all courses in AVAIL_COURSES to the database.'''
    # We can't import the Course model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    global Course
    Course = apps.get_model('coursetracker', 'Course')

    print('')  # so that print statements start on new line
    load_data_files()
    for subject, course_labels in AVAIL_COURSES.items():
        print(f"\tLoading database with courses in {subject}")

        for course_label in course_labels:
            save_course_instance(f"{subject} {course_label}")


class Migration(migrations.Migration):

    dependencies = [
        ('coursetracker', '0015_auto_20210722_1353'),
    ]

    operations = [
        migrations.RunPython(load_courses)
    ]


def load_data_files():
    '''Loads the data files into global variables.'''
    global AVAIL_COURSES, COURSE_INFO, COURSE_STATS, GRADE_DISTRS
    AVAIL_COURSES = _load_json(AVAILABLE_COURSES_FN)
    COURSE_INFO = _load_json(COURSE_INFORMATION_FN)
    COURSE_STATS = _load_json(COURSE_STATISTICS_FN)
    GRADE_DISTRS = _load_json(GRADE_DISTRIBUTIONS_FN)


def _load_json(filename):
    '''Returns the objects stored in a json file.'''
    with open(os.path.join(DATA_DIR_PATH, filename), 'r') as json_file:
        return json.load(json_file)


def save_course_instance(course_name):
    '''Uses the course's information in the global variables to create and save a Course object to the database.'''
    stats = COURSE_STATS[course_name]
    avg = stats['average']
    avg5 = stats['average_past_5_yrs']
    stdev = stats['stdev']
    minavg = stats['min_course_avg']
    maxavg = stats['max_course_avg']
    name = stats['course_title']

    distribution = GRADE_DISTRS[course_name][0]  # first element in list will be from most recent term
    grades = _order_grades(distribution['grades'])
    term = f"{distribution['year']}{distribution['session']}"

    info = COURSE_INFO[course_name] if course_name in COURSE_INFO else {}
    creq = info['creq'] if 'creq' in info else []
    depn = info['depn'] if 'depn' in info else []
    cred = info['cred'] if 'cred' in info else 'n/a'
    desc = info['desc'] if 'desc' in info else 'n/a'
    prer = info['prer'] if 'prer' in info else 'n/a'
    crer = info['crer'] if 'crer' in info else 'n/a'
    link = info['link'] if 'link' in info else 'n/a'

    try:
        with transaction.atomic():
            Course.objects.create(course_name=course_name, average=avg, five_year_average=avg5, lowest_average=minavg,
                                  highest_average=maxavg, standard_deviation=stdev, distribution=grades,
                                  distribution_term=term, corequisites=creq, dependencies=depn, sub_name=name,
                                  number_of_credits=cred, course_description=desc, prerequistes_description=prer,
                                  corequisites_description=crer, course_link=link)
    except IntegrityError:
        pass


def _order_grades(distribution_dict):
    '''Returns a list of the grade distribution. There are 11 elements, in the following order:
        [<50%, 50-54%, 55-59%, 60-63%, 64-67%, 68-71%, 72-75%, 76-79%, 80-84%, 85-89%, 90-100%]
    '''
    grades = list()

    # distribution_dict.values() is already in increasing order, except '<50%' is at the end
    #   - might be because it doesn't start with a number
    grades.append(distribution_dict['<50%'])
    grades.extend(list(distribution_dict.values())[:-1])

    return grades
