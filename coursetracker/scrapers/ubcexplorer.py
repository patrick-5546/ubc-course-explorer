import requests

# Gets relevant statistics from ubcexplorer.io. If invalid course, returns:
#   "Course not found", or "An error has occurred:" + error --> return empty dictionary

api = 'https://ubcexplorer.io/'
allCourseData = {}

# TODO: consider restricting search depth, or storing all required information in txt file, if too slow

# returns the whole prerequisite tree for a subject, including course information, to use, *****set isFirstCall = True*****
#
# return example for MATH 100:
# {
#   "dept": "MATH",
#   "code": "MATH 100",
#   "name": "MATH",
#   "name": "Differential Calculus with Applications to Physical Sciences and Engineering",
#   "cred": 3,
#   "desc": "Derivatives of elementary functions. Applications and modelling: graphing, optimization. Consult the Faculty of Science Credit Exclusion List: www.calendar.ubc.ca/vancouver/index.cfm?tree=12,215,410,414. [3-0-0]",
#   "prer": "High-school calculus and one of (a) a score of 80% or higher in BC Principles of Mathematics 12 or Pre-calculus 12, or (b) a satisfactory score in the UBC Mathematics Basic Skills Test.",
#   "link": "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-course&dept=MATH&course=100,
#   "creq": [],
#   "depn": [],
#   "preq": [], - will contain more course objects (nested)
# }
def course_info_with_prereq_tree(subject, course, isFirstCall=None):
    # resetting allCourseData every call
    if isFirstCall is not None:
        allCourseData = {}

    # obtain information on the course
    courseInfo = course_info(subject, course)
    if courseInfo:
        preq = []
        for pr in courseInfo['preq']:
            subAndCourse = pr.split(" ")
            info = course_info(subAndCourse[0], subAndCourse[1])['preq']
            if info:
                if pr in allCourseData:
                    prereqInfo = allCourseData[pr]
                else:
                    prereqInfo = preq.append(course_info_with_prereq_tree(subject=subAndCourse[0], course=subAndCourse[1])['preq'])
                    # cache information so we don't need to query the same course
                    allCourseData[pr] = prereqInfo
            else:
                preq.append(pr)

        courseInfo['preq'] = preq
    
    return courseInfo

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
