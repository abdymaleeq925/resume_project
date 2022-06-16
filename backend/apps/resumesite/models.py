from django.db import models
from backend.apps.accounts.models import *


class ResumeTemplate(models.Model):
    name = models.CharField(max_length=300)
    template_image = models.ImageField(upload_to='cv_samples/', null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        try:
            old = ResumeTemplate.objects.get(id=self.id)
            
            if old.template_image != self.template_image:
                old.template_image.delete(save=False)
        except:
            pass
        super().save(*args, **kwargs)

class CV(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="cvs")
    first_name = models.CharField("Имя", max_length=50)
    last_name = models.CharField("Фамилия", max_length=50)
    photo = models.ImageField("Фото", upload_to="user/images/", null=True, blank=True)
    email = models.EmailField("Электронная почта")
    mobile = models.CharField("Номер телефона", max_length=15)
    address = models.CharField("Адрес", max_length=200)
    location = models.CharField("Страна", max_length=50)
    prof_summary = models.TextField("О себе", max_length=400)
    resume_template = models.ForeignKey(ResumeTemplate, on_delete=models.CASCADE)


class Education(models.Model):
    HIGHSCHOOL = "highschool"
    BACHELOR = "bachelor"
    MASTER = "master"
    DOCTORATE = "doctorate"
    DEGREES = [
        (HIGHSCHOOL, "Школа"),
        (BACHELOR, "Бакалавр"),
        (MASTER, "Магистратура"),
        (DOCTORATE, "Докторантура")
    ]
    resume = models.ForeignKey(CV, on_delete=models.CASCADE, related_name="education")
    school = models.CharField("Название школы", max_length=100)
    degree = models.CharField("Степень", max_length=12, choices=DEGREES)
    fieldstudy = models.CharField("Специальность", max_length=100)
    start_date = models.DateField("Начало")
    end_date = models.DateField("Конец", null=True, blank=True)

class Experience(models.Model):
    resume = models.ForeignKey(CV, on_delete=models.CASCADE, related_name="experience")
    job_title = models.CharField("Профессия", max_length=100)
    company_name = models.CharField("Название компании", max_length=100)
    job_location = models.CharField("Место работы", max_length=100)
    start_date = models.DateField("Начало")
    end_date = models.DateField("Конец", null=True, blank=True)
    job_description = models.TextField("Описание")

class Skill(models.Model):
    resume = models.ForeignKey(CV, on_delete=models.CASCADE, related_name="skill")
    name = models.CharField(max_length=100)

class Language(models.Model):
    name = models.CharField("Название", max_length=100)

class LanguageCV(models.Model):

    BEGINNER = "beginner"
    ELEMENTARY = "elementary"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
    FLUENT = "fluent"
    LEVEL = [
        (BEGINNER, "Начинайющий"),
        (ELEMENTARY, "Элементарный"),
        (INTERMEDIATE, "Средний"),
        (ADVANCED, "Продвинутый"),
        (FLUENT, "Совершенный")
    ]

    resume = models.ForeignKey(CV, on_delete=models.CASCADE, related_name="language")
    language = models.ForeignKey(Language, on_delete=models.DO_NOTHING, related_name="languagecv")
    level = models.CharField("Уровень", max_length=12, choices=LEVEL)   