import json
from django.shortcuts import redirect, render
from .models import Course
from .scrapers import ubcexplorer as ex, ubcgrades as gr, ratemyprof as rmp

path_to_rmp_data = 'coursetracker/scrapers/rmp_ubc_profs_list.txt'

# search works as a "buffer" for when we are obtaining data
def search(request):
    if request.method == 'GET':
        search = request.GET.get('find')
        #print('search', search)
        return redirect('coursetracker:course', pk=search)

def course(request, pk):
        c = None
        try:
            c = Course.objects.get(course_name__iexact=pk) # case insensitive search
            #print("getting course")
        except Course.DoesNotExist:
            c = create_course(searchedString=pk)
            #print("creating new course")
            if not c:
                return render(request, 'coursetracker/404.html')

        return render(request, 'coursetracker/course.html', {'course': c})

def create_course(searchedString):
    subAndCourse = searchedString.split(' ')
    if len(subAndCourse) == 2:
        subject = subAndCourse[0].upper()
        course = subAndCourse[1]
    else:
        subject = searchedString[0:-3].upper()
        course = searchedString[-3:]

    if not gr.subject_is_valid(subject) or not gr.course_is_valid(subject, course):
        return None

    # TODO: decide whether to get term grade statistics (for high, low, pass, fail, etc.)
    stats = gr.course_statistics(subject, course)
    avg = stats['average']
    avg5 = stats['average_past_5_yrs']
    stdev = stats['stdev']

    # TODO: consider differentiating between no data and 0
    disInfo = gr.latest_distribution_info(subject, course)
    distribution = [grade if grade else 0 for grade in list(disInfo['grades'].values())]
    disTerm = disInfo['year'] + disInfo['session']
    
    ubcProfs = []
    try:
        with open(path_to_rmp_data) as json_file:
            ubcProfs = json.load(json_file)
    except OSError:
        return None
    
    profsList = gr.teaching_team(subject, course)
    profs = rmp.get_profs_info(ubcProfs, profsList)

    exp = ex.course_info_with_prereq_tree(subject, course)
    preq = exp['preq'] 
    creq = exp['creq']
    depn = exp['depn']
    name = exp['name']
    cred = exp['cred']
    desc = exp['desc']
    prer = "n/a" if 'prer' not in exp else exp['prer']
    crer = "n/a" if 'crer' not in exp else exp['crer']
    link = exp['link']

    c = Course(course_name=subject + ' ' + course, average=avg, five_year_average=avg5, standard_deviation=stdev,
                distribution=distribution, distribution_term=disTerm, professors_info=profs, prerequisites=preq, corequisites=creq,
                dependencies=depn, name=name, number_of_credits=cred, course_description=desc,
                prerequistes_description=prer, corequisites_description=crer, course_link=link)
    c.save()
    return c