# Generated by Django 3.2.9 on 2022-06-15 07:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='user/images/', verbose_name='Фото')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('mobile', models.CharField(max_length=15, verbose_name='Номер телефона')),
                ('address', models.CharField(max_length=200, verbose_name='Адрес')),
                ('location', models.CharField(max_length=50, verbose_name='Страна')),
                ('prof_summary', models.TextField(max_length=400, verbose_name='О себе')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='ResumeTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('template_image', models.ImageField(upload_to='cv_samples/')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skill', to='resumesite.cv')),
            ],
        ),
        migrations.CreateModel(
            name='LanguageCV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('beginner', 'Начинайющий'), ('elementary', 'Элементарный'), ('intermediate', 'Средний'), ('advanced', 'Продвинутый'), ('fluent', 'Совершенный')], max_length=12, verbose_name='Уровень')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='languagecv', to='resumesite.language')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='language', to='resumesite.cv')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=100, verbose_name='Профессия')),
                ('company_name', models.CharField(max_length=100, verbose_name='Название компании')),
                ('job_location', models.CharField(max_length=100, verbose_name='Место работы')),
                ('start_date', models.DateField(verbose_name='Начало')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Конец')),
                ('job_description', models.TextField(verbose_name='Описание')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experience', to='resumesite.cv')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=100, verbose_name='Название школы')),
                ('degree', models.CharField(choices=[('highschool', 'Школа'), ('bachelor', 'Бакалавр'), ('master', 'Магистратура'), ('doctorate', 'Докторантура')], max_length=12, verbose_name='Степень')),
                ('fieldstudy', models.CharField(max_length=100, verbose_name='Специальность')),
                ('start_date', models.DateField(verbose_name='Начало')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Конец')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='education', to='resumesite.cv')),
            ],
        ),
        migrations.AddField(
            model_name='cv',
            name='resume_template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resumesite.resumetemplate'),
        ),
        migrations.AddField(
            model_name='cv',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cvs', to=settings.AUTH_USER_MODEL),
        ),
    ]
