# Generated by Django 3.2.9 on 2022-06-23 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumesite', '0003_remove_cv_resume_template'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumetemplate',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
