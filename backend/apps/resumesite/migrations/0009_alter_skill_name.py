# Generated by Django 3.2.9 on 2022-06-30 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumesite', '0008_cv_resume_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Умения'),
        ),
    ]