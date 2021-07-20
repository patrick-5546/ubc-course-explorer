'''Updating local data requires internet connectivity'''


import json

import ubcexplorer as exp
import ubcgrades as gr
import ratemyprof as rmp


# To update Rate My Prof (rmp) data (takes a couple minutes):
ubcProfs = rmp.RateMyProfScraper(1413)  # 1413 is the school ID for UBC on Rate My Prof
ubcProfs.update_rmp_data()

# To update UBC Explorer (exp) data:
with open('coursetracker/scrapers/local_data/exp_courses_list.txt', 'w') as outfile:
    json.dump(exp.courses_info(), outfile)

# To update UBC Grades (gr) data (takes a couple minutes):
for subject in gr.get_api_subjects():
    # Course statistics:
    courseStatistics = gr.all_course_statistics(subject)
    if courseStatistics:
        with open('coursetracker/scrapers/local_data/gr_course-statistics/' + subject + '.txt', 'w') as outfile:
            json.dump(courseStatistics, outfile)

    # Distributions:
    distributions = gr.all_distribution_info(subject)
    if distributions:
        with open('coursetracker/scrapers/local_data/gr_distributions/' + subject + '.txt', 'w') as outfile:
            json.dump(distributions, outfile)

    # Teaching team:
    teachingTeam = gr.all_teaching_team(subject)
    if teachingTeam:
        with open('coursetracker/scrapers/local_data/gr_teaching-team/' + subject + '.txt', 'w') as outfile:
            json.dump(teachingTeam, outfile)

    # Courses List:
    allSubjectCourses = gr.get_api_courses(subject)
    if allSubjectCourses:
        with open('coursetracker/scrapers/local_data/gr_subject-course-list/' + subject + '.txt', 'w') as outfile:
            json.dump(allSubjectCourses, outfile)

gr.refresh_all_section_distributions()
