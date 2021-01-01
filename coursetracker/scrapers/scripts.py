#To test nested prereq tree: 256 -> 223 -> 121 -> 120, 100, ...
import ubcexplorer as exp
print(exp.nested_preq_helper("math 100"))
# print(len(exp.allCourseData))
# print(exp.count)
# print(exp.course_info("math", "256")['preq'])

#To update rmp data (will take a while):
# import ratemyprof as rmp
# rmp.ubcProfs.update_rmp_data()

#To test distributions
# import ubcgrades as gr
# disInfo = gr.distributions("math", "101")
# print([grade if grade else 0 for grade in list(disInfo['grades'].values())])