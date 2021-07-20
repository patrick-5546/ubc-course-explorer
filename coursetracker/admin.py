from django.contrib import admin

from .models import Course


class CourseAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['course_name']}),
        ('Descriptions', {'fields': ['sub_name', 'course_description', 'prerequistes_description',
                                     'corequisites_description', 'course_link']}),
        ('Course Profile', {'fields': ['five_year_average', 'standard_deviation',
                                       'number_of_credits']}),
        ('Graphing Information', {'fields': ['distribution_term', 'distribution']}),
        ('Related Courses', {'fields': ['corequisites', 'dependencies']})
    ]
    # fields to display in page that displays all questions
    list_display = ('course_name', 'five_year_average')
    search_fields = ['course_name']  # search textbox by question_text


# If you want to add to admin home page
admin.site.register(Course, CourseAdmin)
