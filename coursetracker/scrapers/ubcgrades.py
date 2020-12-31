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
    caps_subject = subject.upper() + '/'
    url = apiV2 + campus + caps_subject + course
    return check_json(requests.get(url).json())

# return example element for 2019W of SCIE 001 (returns array where each element is a term):
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
def distributions(subject, course):
    caps_subject = subject.upper() + '/'
    url = apiV2 + 'distributions/' + campus + caps_subject + course
    return check_json(requests.get(url).json())

# return example element for Yurika Aonuki of LING 100 (returns array where each element is a person):
# {
#   "campus":"UBCV",
#   "course":"100",
#   "detail":"",
#   "name":"Yurika Aonuki",
#   "subject":"LING",
#   "yearsessions":{"2020S":1}
# }
def teaching_team(subject, course):
    caps_subject = subject.upper() + '/'
    url = apiV2 + 'teaching-team/' + campus + caps_subject + course
    return check_json(requests.get(url).json())

def check_json(j):
    return {} if 'error' in json.dumps(j) else j

# TODO: decide whether to implement drop down menus


apiV1 = 'https://ubcgrades.com/api/v1/'

# checks if given subject is valid
def subject_is_valid(subject):
    caps_subject = subject.upper()
    url = apiV1 + 'subjects/UBCV'
    allSubjects = requests.get(url).json()
    return True if caps_subject in [subjectInfo['subject'] for subjectInfo in allSubjects] else False

# checks if given course is valid
def course_is_valid(subject, course):
    caps_subject = subject.upper()
    url = apiV1 + 'courses/' + campus + caps_subject
    allCourses = requests.get(url).json()
    return True if course in [courseInfo['course'] for courseInfo in allCourses] else False