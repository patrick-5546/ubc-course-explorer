from django.http import JsonResponse
from django.shortcuts import redirect, render

from .models import Course
from .serializers import CourseSerializer


def search(request):
    '''Works as a "buffer" for when we are obtaining data'''
    if request.method == 'GET':
        search = request.GET.get('find')
        course_name = search.upper()  # make search query uppercase
        print(f"*Searching database for {course_name}")
        return redirect('coursetracker:course', course_name)


def course(request, course_name):
    '''Finds the Course object from its course name, returning that course's page if it exists.

    Inputs:
        - course_name (str): must be in the format '<subject> <number><detail>', all caps
            - Not all course names have details
            - Examples: MATH 100, APSC 496D
    '''
    try:
        c = Course.objects.get(course_name__exact=course_name)
        print(f"*{course_name} found in database")
    except Course.DoesNotExist:
        print(f"*Course {course_name} does not exist")
        return render(request, 'coursetracker/404.html')

    return render(request, 'coursetracker/course.html', {'course': c})


def all_courses_api(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return JsonResponse(serializer.data, safe=False)


def course_api(request, course_name):
    try:
        c = Course.objects.get(course_name__exact=course_name)
        print(f"*{course_name} found in database")
    except Course.DoesNotExist:
        print(f"*Course {course_name} does not exist")
        return render(request, 'coursetracker/404.html')

    serializer = CourseSerializer(c)
    return JsonResponse(serializer.data, json_dumps_params={'indent': 2})
