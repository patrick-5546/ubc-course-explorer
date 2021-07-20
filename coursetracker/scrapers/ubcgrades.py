'''Gets relevant statistics from ubcgrades.com. If invalid course, returns:
{"error":"Not Found","message":"Not Found"} --> return an empty dictionary
'''


import json
import requests

apiV2 = 'https://ubcgrades.com/api/v2/course-statistics/'
apiV1 = 'https://ubcgrades.com/api/v1/'
campus = 'UBCV/'


def course_statistics(subject, course):
    '''Return example for ENGL 112:
    {
    "average":71.36852382490527,
    "average_past_5_yrs":73.02862580894177,
    "campus":"UBCV",
    "course":"112",
    "course_title":"Strategies for University Writing",
    "detail":"",
    "faculty_title":"Faculty of Arts",
    "max_course_avg":86.09,
    "min_course_avg":57.76,
    "stdev":9.868147070294798,
    "subject":"ENGL",
    "subject_title":"English"
    }
    '''
    subjectCourseInfo = []
    try:
        with open('coursetracker/scrapers/local_data/gr_course-statistics/' + subject.upper() + '.txt') as json_file:
            subjectCourseInfo = json.load(json_file)
    except OSError:
        pass
    for courseInfo in subjectCourseInfo:
        if courseInfo['course'] == course:
            return courseInfo
    return {}


def all_course_statistics(subject):
    url = apiV2 + campus + subject.upper()
    return check_json(requests.get(url).json())


def latest_distribution_info(subject, course):
    '''Return example for 2019W of SCIE 001:
    {
    "campus":"UBCV",
    "course":"001",
    "detail":"",
    "grades":{"0-9%":"","10-19%":"","20-29%":"","30-39%":"","40-49%":"","50-54%":"","55-59%":"","60-63%":"",
                "64-67%":"","68-71%":"","72-75%":"","76-79%":9,"80-84%":16,"85-89%":19,"90-100%":27,"<50%":""},
    "session":"W",
    "subject":"SCIE",
    "year":"2019"
    }
    '''
    subjectCourseInfo = []
    try:
        with open('coursetracker/scrapers/local_data/gr_distributions/' + subject.upper() + '.txt') as json_file:
            subjectCourseInfo = json.load(json_file)
    except OSError:
        pass
    availableDistributions = []
    for courseInfo in subjectCourseInfo:
        if courseInfo['course'] == course:
            availableDistributions.append(courseInfo)
    if availableDistributions:
        # prefer winter term distribution
        i = len(availableDistributions) - 1
        dis = availableDistributions[i]
        while dis['session'] != 'W' and i > 1:
            i -= 1
            dis = availableDistributions[i]
        return availableDistributions[len(availableDistributions) - 1] if i == 0 else dis
    else:
        return availableDistributions


def all_distribution_info(subject):
    url = apiV2 + 'distributions/' + campus + subject.upper()
    return check_json(requests.get(url).json())


def teaching_team(subject, course):
    '''Returns a list of all the named educators (profs and TAs) who have taught the course'''
    subjectCourseInfo = []
    try:
        with open('coursetracker/scrapers/local_data/gr_teaching-team/' + subject.upper() + '.txt') as json_file:
            subjectCourseInfo = json.load(json_file)
    except OSError:
        pass
    allProfsInfo = []
    for courseInfo in subjectCourseInfo:
        if courseInfo['course'] == course:
            allProfsInfo.append(courseInfo)
    return [profInfo['name'] for profInfo in allProfsInfo if profInfo['name']] if allProfsInfo else {}


def all_teaching_team(subject):
    url = apiV2 + 'teaching-team/' + campus + subject.upper()
    return check_json(requests.get(url).json())


def recent_sections_taught(profsList, subject, course):
    '''Returns a dictionary where the keys are the professor name and the values are a list of sections
    taught from 2016-2018
    '''
    profsDict = {prof: [] for prof in profsList}
    allDistributions = []
    try:
        with open('coursetracker/scrapers/local_data/gr_section_distributions.txt') as json_file:
            allDistributions = json.load(json_file)
    except OSError:
        return profsDict
    for prof in profsList:
        firstLast = prof.split(' ')
        if len(firstLast) != 2:
            continue
        name = firstLast[1] + ', ' + firstLast[0]
        for d in allDistributions:
            if subject.upper() == d['subject'] and course == d['course'] and name in d['educators'] and \
                    d['section'] not in profsDict[prof]:
                profsDict[prof].append(d['section'])
    return profsDict


def refresh_all_section_distributions():
    yearsessions = ['2016S', '2016W', '2017S', '2017W', '2018S', '2018W']
    allDistributions = []
    for yearsession in yearsessions:
        url = apiV1 + 'grades/' + campus + yearsession
        yearsessionDistributions = check_json(requests.get(url).json())
        if yearsessionDistributions:
            allDistributions += yearsessionDistributions
    if allDistributions:
        with open('coursetracker/scrapers/local_data/gr_section_distributions.txt', 'w') as outfile:
            json.dump(allDistributions, outfile)


def check_json(j):
    return {} if 'error' in json.dumps(j) else j


def course_is_valid(subject, course):
    '''Checks if given course is valid'''
    subjectCourses = []
    try:
        with open('coursetracker/scrapers/local_data/gr_subject-course-list/' + subject.upper() + '.txt') as json_file:
            subjectCourses = json.load(json_file)
    except OSError:
        pass
    for courseNum in subjectCourses:
        if courseNum == course:
            return True
    return False


def get_api_subjects():
    '''Get list of all subjects available'''
    url = apiV1 + 'subjects/UBCV'
    allSubjects = check_json(requests.get(url).json())
    return [subjectInfo['subject'] for subjectInfo in allSubjects] if allSubjects else []


def get_api_courses(subject):
    '''Get list of all courses available for a subject'''
    caps_subject = subject.upper()
    url = apiV1 + 'courses/' + campus + caps_subject
    allCourses = check_json(requests.get(url).json())
    return [courseInfo['course'] for courseInfo in allCourses] if allCourses else []
