from django.shortcuts import redirect, render
from .models import Course
from .scrapers import ubcexplorer as ex, ubcgrades as gr, ratemyprof as rmp


def search(request):
    '''Works as a "buffer" for when we are obtaining data'''
    if request.method == 'GET':
        search = request.GET.get('find')
        # print('search', search)
        return redirect('coursetracker:course', pk=search)


def course(request, pk):
    # initializing course_name so that the subject is all caps
    course_name = pk
    course_name_list = pk.split(' ')
    if len(course_name_list) == 2:
        course_name = f"{course_name_list[0].upper()} {course_name_list[1]}"

    try:
        c = Course.objects.get(course_name__exact=course_name)
    except Course.DoesNotExist:
        return render(request, 'coursetracker/404.html')

    subject, course = course_name.split(' ')
    exp = ex.course_info_with_prereq_tree(subject, course)
    preq = {} if 'preq' not in exp else exp['preq']
    preq = {course_name: preq}  # dictionary for tree chart

    profsList = gr.teaching_team(subject, course)

    profs = rmp.get_profs_info(profsList)  # list for sortable list
    if not profs:
        return render(request, 'coursetracker/404.html')  # TODO: make separate html page for this

    profsSecInfo = gr.recent_sections_taught(profsList, subject, course)
    sectionProfs = {}
    for prof in profsSecInfo:
        for sec in profsSecInfo[prof]:
            if sec not in sectionProfs:
                sectionProfs[sec] = []
            sectionProfs[sec].append(prof)
    sectionProfsSorted = {sec: sectionProfs[sec] for sec in sorted(sectionProfs)}

    return render(request, 'coursetracker/course.html', {'course': c, 'preq': preq, 'professors_info': profs,
                                                         'sections_taught': sectionProfsSorted})
