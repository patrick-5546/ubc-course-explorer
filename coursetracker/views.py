import json
from django.shortcuts import redirect, render
from .models import Course
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
            c = Course.objects.get(course_name__iexact=pk) # case insensitive search
            #print("getting course")
        except Course.DoesNotExist:
            c = create_course(searchedString=pk)
            #print("creating new course")
            if not c:
                return render(request, 'coursetracker/404.html')

        subAndCourse = pk.split(' ')
        if len(subAndCourse) == 2:
            subject = subAndCourse[0].upper()
            course = subAndCourse[1]
        else:
            subject = pk[0:-3].upper()
            course = pk[-3:]

        exp = ex.course_info_with_prereq_tree(subject, course)
        preq = "n/a" if 'preq' not in exp else exp['preq'] 

        return render(request, 'coursetracker/course.html', {'course': c, 'preq': preq})

def create_course(searchedString):
    subAndCourse = searchedString.split(' ')
    if len(subAndCourse) == 2:
        subject = subAndCourse[0].upper()
        course = subAndCourse[1]
    else:
        subject = searchedString[0:-3].upper()
        course = searchedString[-3:]

    if not gr.course_is_valid(subject, course):
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
    
    profsList = gr.teaching_team(subject, course)
    profs = rmp.get_profs_info(profsList)
    if not profs:
        print('Unable to read rmp data from file')  # TODO: make separate html page for this
        return None

    exp = ex.course_info_with_prereq_tree(subject, course)
    preq = "n/a" if 'preq' not in exp else exp['preq'] 
    creq = "n/a" if 'creq' not in exp else exp['creq']
    depn = "n/a" if 'depn' not in exp else exp['depn']
    name = "n/a" if 'name' not in exp else exp['name']
    cred = "n/a" if 'cred' not in exp else exp['cred']
    desc = "n/a" if 'desc' not in exp else exp['desc']
    prer = "n/a" if 'prer' not in exp else exp['prer']
    crer = "n/a" if 'crer' not in exp else exp['crer']
    link = "n/a" if 'link' not in exp else exp['link']

    c = Course(course_name=subject + ' ' + course, average=avg, five_year_average=avg5, standard_deviation=stdev,
                distribution=distribution, distribution_term=disTerm, professors_info=profs, 
                prerequisites=preq, corequisites=creq, dependencies=depn, sub_name=name, number_of_credits=cred,
                course_description=desc, prerequistes_description=prer, corequisites_description=crer, course_link=link)
    c.save()
    return c
