'''Gets relevant statistics from ubcexplorer.io. If invalid course, returns:
"Course not found", or "An error has occurred:" + error --> return empty dictionary
'''


import json
import requests

allCourseData = {}
expData = []
try:
    with open('coursetracker/scrapers/local_data/exp_courses_list.txt') as json_file:
        expData = json.load(json_file)
except OSError:
    pass


def course_info_with_prereq_tree(subject, course):
    '''Returns the whole prerequisite tree for a subject, including course information

    return example for MATH 210:
    {
    "preq": [], - will contain more course objects (nested)
    "creq": [ "MATH 215", "MATH 255", "MATH 256", "MATH 258", "MATH 152", "MATH 221", "MATH 223"],
    "depn": [ "CPSC 203", "CPSC 330", "EOSC 442"],
    "_id": "5eb76d718ade8b27172d6363",
    "dept": "MATH",
    "code": "MATH 210",
    "name": "Introduction to Mathematical Computing",
    "cred": 3,
    "desc": "Course Description",
    "prer": "One of MATH 101, MATH 103, MATH 105, MATH 121, SCIE 001.",
    "crer": "One of MATH 215, MATH 255, MATH 256, MATH 258 and one of MATH 152, MATH 221, MATH 223.",
    "link": "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-course&dept=MATH&course=210"
    }
    '''
    courseInfo = course_info(subject, course)
    code = subject.upper() + ' ' + course
    courseInfo['preq'] = nested_preq_helper(code)

    return courseInfo


def nested_preq_helper(str):
    '''Returns a dictionary with all the prerequisites required
    - Example path: MATH 256 has prerequisite 223 which has prerequisite 121
        which has prerequisite 120 which has no prerequisites
        - Represented by: {..., MATH 223: {MATH 121: {MATH 120: {}, ...}, ...}}
    '''
    global expData
    global allCourseData

    subAndCourse = str.split(' ')
    code = subAndCourse[0].upper() + ' ' + subAndCourse[1]

    courseInfo = course_info(subAndCourse[0], subAndCourse[1])
    preq = courseInfo['preq'] if courseInfo else {}
    if preq:
        if code in allCourseData:  # load from cache to save time
            return allCourseData[code]
        else:
            nestedPreqs = {course: nested_preq_helper(course) for course in preq}
            allCourseData[code] = nestedPreqs
            return nestedPreqs
    else:
        return preq


def course_info(subject, course):
    '''See course_info_with_prereq tree documentation
    Difference is that "preq" field only contains immediate prerequisites
    '''
    global expData

    caps_subject = subject.upper()
    for courseInfo in expData:
        if courseInfo['code'] == caps_subject + ' ' + course:
            return courseInfo
    return {}


def courses_info():
    '''Returns all course info on UBC Explorer'''
    url = 'https://ubcexplorer.io/getAllCourses/'
    r = requests.get(url)
    try:
        coursesInfo = r.json()
        return coursesInfo
    except ValueError:
        return {}
