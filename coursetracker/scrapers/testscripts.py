#To test nested prereq tree: 256 -> 223 -> 121 -> 120, 100, ...
# import ubcexplorer as exp
# print(exp.nested_preq_helper("math 100"))
# print(len(exp.allCourseData))
# print(exp.count)
# print(exp.course_info("math", "256")['preq'])

#To test distributions
# import ubcgrades as gr
# disInfo = gr.distributions("math", "101")
# print([grade if grade else 0 for grade in list(disInfo['grades'].values())])

#To test rmp data:
# import ratemyprof as rmp, json
# ubcProfs = []
# with open('coursetracker/scrapers/rmp_ubc_profs_list.txt') as json_file:
#     ubcProfs = json.load(json_file)
# profsList = ['Robert Gateman', 'Tor Aamodt']
# print(rmp.get_profs_info(ubcProfs, profsList))