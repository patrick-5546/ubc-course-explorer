from django.shortcuts import redirect, render

from .models import Course
from .scrapers import ratemyprof as rmp
from .scrapers import ubcexplorer as ex
from .scrapers import ubcgrades as gr


# search works as a "buffer" for when we are obtaining data
def search(request):
    if request.method == 'GET':
        search = request.GET.get('find')
        print('search', search)
        return redirect('coursetracker:course', pk=search)

def course(request, pk):
        try:
            # case insensitive search
            course = Course.objects.get(course_name__iexact=pk)
            print("getting course")
        except Course.DoesNotExist:
            subAndCourse = str(pk).split(" ")
            subject = subAndCourse[0]
            course = subAndCourse[1]

            # stats = gr.course_statistics(subject, course)
            # avg = float(stats['average'])
            # avg5 = float(stats['average_past_5_yrs'])
            # stdev = float(stats['stdev'])
            # print(stats)
            # print(avg)
            # print(avg5)
            # print(stdev)

            distributions = gr.distributions(subject, course)  # need to process this, turn into graph
            profs = gr.teaching_team(subject, course)  # need to process this, sort by rating and tNumRatings
            print(distributions)
            print(profs)

            # exp = ex.course_info_with_prereq_tree(subject, course, True)
            # preq = exp['preq']  # need to process this, turn into tree
            # creq = exp['creq']
            # depn = exp['depn']
            # name = exp['name']
            # cred = exp['cred']
            # desc = exp['desc']
            # prer = exp['prer']
            # crer = exp['crer']
            # link = exp['link']

            course = Course(course_name=pk)#, average=avg, five_year_average=avg5, standard_deviation=stdev)#,
                            # distributions=distributions, professors=profs, prerequisites=preq, corequisites=creq,
                            # dependencies=depn, name=name, number_of_credits=cred, course_description=desc,
                            # prerequistes_description=prer, corequisites_description=crer, link=link)
            course.save()
            print("creating new course")

        return render(request, 'coursetracker/course.html', {'course': course})
