import requests

# Gets relevant statistics from ubcexplorer.io. If invalid course, returns:
#   "Course not found", or "An error has occurred:" + error --> return empty dictionary

api = 'https://ubcexplorer.io/'
allCourseData = {}

# TODO: consider storing all required information (especially preq) in global variable to increase speed
# TODO: modify to save node -- [node [child1, [child2, [child21, child22]], child3]
#       Currently, only saves leaf nodes -- [child1, child21, child22, child3]

# returns the whole prerequisite tree for a subject, including course information, to use, *****set isFirstCall = True*****
#
# return example for MATH 210:
# {
#   "preq": [], - will contain more course objects (nested)
#   "creq": [ "MATH 215", "MATH 255", "MATH 256", "MATH 258", "MATH 152", "MATH 221", "MATH 223"],
#   "depn": [ "CPSC 203", "CPSC 330", "EOSC 442"],
#   "_id": "5eb76d718ade8b27172d6363",
#   "dept": "MATH",
#   "code": "MATH 210",
#   "name": "Introduction to Mathematical Computing",
#   "cred": 3,
#   "desc": "Course Description",
#   "prer": "One of MATH 101, MATH 103, MATH 105, MATH 121, SCIE 001.",
#   "crer": "One of MATH 215, MATH 255, MATH 256, MATH 258 and one of MATH 152, MATH 221, MATH 223.",
#   "link": "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-course&dept=MATH&course=210"
# }
def course_info_with_prereq_tree(subject, course):
    courseInfo = course_info(subject, course)
    code = subject + ' ' + course
    courseInfo['preq'] = nested_preq_helper(code)
    
    return courseInfo

def nested_preq_helper(code):
    global allCourseData
    subAndCourse = code.split(' ')
    preq = course_info(subAndCourse[0], subAndCourse[1])['preq']
    if preq:
        if code in allCourseData:  # load from cache to save time
            return allCourseData[code]
        else:
            nestedPreqs = {}
            for course in preq:
                nestedPreqs[course] = nested_preq_helper(course)
            allCourseData[code] = nestedPreqs
            return nestedPreqs
    else:
        return {}

def course_info(subject, course):
    caps_subject = subject.upper()
    url = api + 'getCourseInfo/' + caps_subject + '%20' + course
    r = requests.get(url)
    try:
        response = r.json()
        return response
    except ValueError:
        return {}

# TODO: decide whether to implement this
"""
# returns all course data for drop down menus
def courses():
    url = api + 'getAllCourses/'
    r = requests.get(url)
    return r.json()
"""
