from django.urls import path

from . import views

app_name = 'coursetracker'

urlpatterns = [
    path('search', views.search, name="search"),
    path('view/<str:course_name>', views.course, name="course"),
    path('all_courses_api', views.all_courses_api),
    path('course_api/<str:course_name>', views.course_api)
]
