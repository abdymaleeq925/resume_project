# Generated by Django 3.2.9 on 2022-07-06 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resumesite', '0010_language_resume'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='language',
            name='resume',
        ),
    ]
