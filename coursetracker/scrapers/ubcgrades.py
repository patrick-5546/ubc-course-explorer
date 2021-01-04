import requests, json

# Gets relevant statistics from ubcgrades.com. If invalid course, returns:
#   {"error":"Not Found","message":"Not Found"} --> return an empty dictionary

apiV2 = 'https://ubcgrades.com/api/v2/course-statistics/'
campus = 'UBCV/'

# return example for ENGL 112:
# {
#   "average":71.36852382490527,
#   "average_past_5_yrs":73.02862580894177,
#   "campus":"UBCV",
#   "course":"112",
#   "course_title":"Strategies for University Writing",
#   "detail":"",
#   "faculty_title":"Faculty of Arts",
#   "max_course_avg":86.09,
#   "min_course_avg":57.76,
#   "stdev":9.868147070294798,
#   "subject":"ENGL",
#   "subject_title":"English"
# }
def course_statistics(subject, course):
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

# return example for 2019W of SCIE 001:
# {
#   "campus":"UBCV",
#   "course":"001",
#   "detail":"",
#   "grades":{"0-9%":"","10-19%":"","20-29%":"","30-39%":"","40-49%":"","50-54%":"","55-59%":"","60-63%":"",
#             "64-67%":"","68-71%":"","72-75%":"","76-79%":9,"80-84%":16,"85-89%":19,"90-100%":27,"<50%":""},
#   "session":"W",
#   "subject":"SCIE",
#   "year":"2019"
# }
def latest_distribution_info(subject, course):
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

# returns a list of all the named educators (profs and TAs) who have taught the course
def teaching_team(subject, course):
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

# returns a dictionary where the keys are the professor name and the values are a list of sections 
# taught from 2016-2018
def recent_sections_taught(profsList, subject, course):
    caps_subject = subject.upper() + '/'
    yearsessions = ['2016S/', '2016W', '2017S/', '2017W/', '2018S/' ,'2018W/']
    profsDict = {prof: [] for prof in profsList}
    for yearsession in yearsessions:
        url = apiV1 + 'grades/' + campus + yearsession + caps_subject + course
        allDistributions = check_json(requests.get(url).json())
        for prof in profsList:
            firstLast = prof.split(' ')
            if len(firstLast) != 2:
                continue
            name = firstLast[1] + ', ' + firstLast[0]
            for distribution in allDistributions:
                if name in distribution['educators'] and distribution['section'] not in profsDict[prof]:
                    profsDict[prof].append(distribution['section'])
    return profsDict


def check_json(j):
    return {} if 'error' in json.dumps(j) else j

# TODO: decide whether to implement drop down menus


apiV1 = 'https://ubcgrades.com/api/v1/'

# checks if given course is valid
def course_is_valid(subject, course):
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

# get list of all subjects available
def get_api_subjects():
    url = apiV1 + 'subjects/UBCV'
    allSubjects = check_json(requests.get(url).json())
    return [subjectInfo['subject'] for subjectInfo in allSubjects] if allSubjects else []

# get list of all courses available for a subject
def get_api_courses(subject):
    caps_subject = subject.upper()
    url = apiV1 + 'courses/' + campus + caps_subject
    allCourses = check_json(requests.get(url).json())
    return [courseInfo['course'] for courseInfo in allCourses] if allCourses else []
