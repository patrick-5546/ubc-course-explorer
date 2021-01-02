import ubcexplorer as exp, ubcgrades as gr, ratemyprof as rmp, json

# #To update rmp data (takes a couple minutes):
# ubcProfs = rmp.RateMyProfScraper(1413)  # 1413 is the school ID for UBC on Rate My Prof
# ubcProfs.update_rmp_data()

# #To update preq data (takes around an hour):
# for subject in gr.get_subjects():
#     subjectCoursesPreqs = {}
#     for course in gr.get_courses(subject):
#         print(subject + ' ' + course)
#         courseInfo = exp.course_info(subject, course)
#         if courseInfo:
#             subjectCoursesPreqs[subject + ' ' + course] = courseInfo['preq']
#     print(subjectCoursesPreqs)
#     if subjectCoursesPreqs:
#         with open('coursetracker/scrapers/exp_all_course_preqs/' + subject + '.txt', 'w') as outfile:
#             json.dump(subjectCoursesPreqs, outfile)
    