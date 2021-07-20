import ubcexplorer as exp
import ubcgrades as gr
import ratemyprof as rmp


# To test nested prereq tree: 256 -> 223 -> 121 -> 120, 100, ...
print(exp.nested_preq_helper("math 256"))
print(len(exp.allCourseData))
print(exp.course_info("math", "256")['preq'])

# To test distributions
disInfo = gr.latest_distribution_info("engl", "112")
print(disInfo)
print([grade if grade else 0 for grade in list(disInfo['grades'].values())])

# To test course retrieval
print(gr.get_subjects())
print(gr.get_courses('cpen'))

# To ubcgrades local data retrieval
print(gr.course_statistics("math", "256"))
print(gr.latest_distribution_info("math", "256"))
profsList = gr.teaching_team("math", "220")
print(profsList)
print(gr.recent_sections_taught(profsList, "math", "220"))

# To test valid
print(gr.course_is_valid('cpen', '221'))  # true
print(gr.course_is_valid('cpen', '22ds1'))  # false

# To test rmp data:
ubcProfs = []
profsList = ['Robert Gateman', 'Tor Aamodt']
print(rmp.get_profs_info(profsList))
