from django.urls import path
from .views import *
from .models import *

urlpatterns = [
    path('', home, name='home'),
    path('service/', service, name='service'),
    path('aboutus/', aboutus, name='aboutus'),
    path('myresumes/', MyResumes.as_view(), name='myresumes'),
    path('template/', ResumeTemplates.as_view(), name='resumetemplates'),
    path('profile/', CVShow.as_view(), name='profile'),
    path('education/<int:pk>/', EduShow.as_view(), name='education'),
    path('del_education/<int:pk>/', DelEduShow, name='del_education'),
    path('experience/<int:pk>', XPShow.as_view(), name='experience'),
    path('experience/', nextpage, name='nextpage'),
    path('skills/<int:pk>', SkillShow.as_view(), name='skills'),
    path('language/<int:pk>', LangShow.as_view(), name='language'),
    path('resume_detail/<int:pk>', ResumeDetailView.as_view(), name="resume_detail"),
    path('education_detail/<int:pk>', EducationDetailView.as_view(), name="education_detail"),
    path('experience_detail/<int:pk>', ExperienceDetailView.as_view(), name="experience_detail"),
    path('export/', export, name="export")
]
