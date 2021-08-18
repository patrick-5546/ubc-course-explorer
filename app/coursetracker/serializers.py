from rest_framework import serializers
from coursetracker.models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_name', 'sub_name', 'course_link', 'average', 'five_year_average', 'standard_deviation',
                  'number_of_credits', 'lowest_average', 'highest_average', 'profile_link', 'distribution',
                  'distribution_term', 'distribution_link', 'sections_teaching_team', 'professor_ratings',
                  'course_description', 'prerequisites_description', 'corequisites_description', 'prerequisite_tree']
