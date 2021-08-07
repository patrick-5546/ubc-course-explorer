from django.contrib import admin

from .models import Course


class CourseAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['course_name', 'sub_name', 'course_link']}),
        ('Course Profile', {'fields': ['average', 'five_year_average', 'standard_deviation', 'number_of_credits',
                                       'lowest_average', 'highest_average', 'profile_link']}),
        ('Graphing Information', {'fields': ['distribution_term', 'distribution', 'distribution_link']}),
        ('Descriptions', {'fields': ['course_description', 'prerequistes_description', 'corequisites_description']}),
        ('Professor Information', {'fields': ['sections_teaching_team', 'professor_ratings']}),
        ('Prerequisite Tree', {'fields': ['prerequisite_tree']})
    ]
    # fields to display in page that displays all questions
    list_display = ('course_name', 'average')
    search_fields = ['course_name']  # search textbox by question_text


# If you want to add to admin home page
admin.site.register(Course, CourseAdmin)
