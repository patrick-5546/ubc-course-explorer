from django.shortcuts import redirect, render

from .models import Course
# TODO: commented out import dramatically slows down actions because it has to generate professor
# list every time --> need to work around this, perhaps store in txt file
from .scrapers import ubcexplorer as ex, ubcgrades as gr, ratemyprof as rmp

# search works as a "buffer" for when we are obtaining data
def search(request):
    if request.method == 'GET':
        search = request.GET.get('find')
        #print('search', search)
        return redirect('coursetracker:course', pk=search)

def course(request, pk):
        c = None
        try:
            # case insensitive search
            c = Course.objects.get(course_name__iexact=pk)
            #print("getting course")
        except Course.DoesNotExist:
            subAndCourse = pk.split(' ')
            if len(subAndCourse) == 2:
                subject = subAndCourse[0]
                course = subAndCourse[1]
            else:
                subject = pk[0:-3] 
                course = pk[-3:]

            if not gr.subject_is_valid(subject) or not gr.course_is_valid(subject, course):
                return render(request, 'coursetracker/404.html')

            # TODO: decide whether to get term grade statistics (for high, low, pass, fail, etc.)
            stats = gr.course_statistics(subject, course)
            avg = stats['average']
            avg5 = stats['average_past_5_yrs']
            stdev = stats['stdev']

            distributions = gr.distributions(subject, course)  # need to process this, turn into graph
            
            profsList = gr.teaching_team(subject, course)
            profs = rmp.ubcProfs.professors_info(profsList)

            exp = ex.course_info_with_prereq_tree(subject, course, True)
            preq = exp['preq']  # need to process this, turn into tree
            creq = exp['creq']
            depn = exp['depn']
            name = exp['name']
            cred = exp['cred']
            desc = exp['desc']
            prer = "n/a" if 'prer' not in exp else exp['prer']
            crer = "n/a" if 'crer' not in exp else exp['crer']
            link = exp['link']

            c = Course(course_name=pk, average=avg, five_year_average=avg5, standard_deviation=stdev,
                       distributions=distributions, professors=profs, prerequisites=preq, corequisites=creq,
                       dependencies=depn, name=name, number_of_credits=cred, course_description=desc,
                       prerequistes_description=prer, corequisites_description=crer, link=link)
            c.save()
            #print("creating new course")

        return render(request, 'coursetracker/course.html', {'course': c})
