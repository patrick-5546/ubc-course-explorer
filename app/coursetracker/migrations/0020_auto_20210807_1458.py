# Generated by Django 3.1.13 on 2021-08-07 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursetracker', '0019_auto_20210728_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='distribution_link',
            field=models.CharField(default='err', max_length=200),
        ),
        migrations.AddField(
            model_name='course',
            name='profile_link',
            field=models.CharField(default='err', max_length=200),
        ),
    ]