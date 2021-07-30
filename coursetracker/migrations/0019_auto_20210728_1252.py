# Generated by Django 3.1.13 on 2021-07-28 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursetracker', '0018_course_prerequisite_tree'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='prerequisite_tree',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='course',
            name='professor_ratings',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='course',
            name='sections_teaching_team',
            field=models.JSONField(default=dict),
        ),
    ]