from django import forms
from .models import *

class ResumeForm(forms.ModelForm):
    class Meta():
       model = ResumeTemplate
       fields = ['name','template_image']


class ProfileForm(forms.ModelForm):
    class Meta():
        model = CV
        fields = ['resume_name', 'first_name', 'last_name', 'photo', 'email', 'mobile', 'address', 'location', 'prof_summary']
        widgets = {
            'resume_name': forms.TextInput(attrs={"class": "form-control"}),
            'first_name': forms.TextInput(attrs={"class": "form-control"}),
            'last_name': forms.TextInput(attrs={"class": "form-control"}),
            'photo': forms.FileInput(attrs={"class": "form-control"}),
            'email': forms.EmailInput(attrs={"class": "form-control"}),
            'mobile': forms.TextInput(attrs={"class": "form-control"}),
            'address': forms.TextInput(attrs={"class": "form-control"}),
            'location': forms.TextInput(attrs={"class": "form-control"}),
            'prof_summary': forms.Textarea(attrs={"class": "form-control"})
        }

class EducationForm(forms.ModelForm):
    degree = forms.ChoiceField(widget=forms.Select(attrs={"class":"form-control"}), choices=Education.DEGREES)

    class Meta():
        model = Education
        fields = ['school', 'degree', 'fieldstudy', 'start_date', 'end_date']
        widgets = {
            'school': forms.TextInput(attrs={"class": "form-control"}),
            'degree': forms.TextInput(attrs={"class": "form-control"}),
            'fieldstudy': forms.TextInput(attrs={"class": "form-control"}),
            'start_date': forms.DateInput(attrs={"class": "form-control", "type":"date"}),
            'end_date': forms.DateInput(attrs={"class": "form-control", "type":"date"})
        }


class XPForm(forms.ModelForm):
    class Meta():
        model = Experience
        fields = ['job_title', 'company_name', 'job_location', 'start_date', 'end_date', 'job_description']
        widgets = {
            'job_title': forms.TextInput(attrs={"class": "form-control"}),
            'company_name': forms.TextInput(attrs={"class": "form-control"}),
            'job_location': forms.TextInput(attrs={"class": "form-control"}),
            'start_date': forms.DateInput(attrs={"class": "form-control", "type":"date"}),
            'end_date': forms.DateInput(attrs={"class": "form-control", "type":"date"}),
            'job_description': forms.Textarea(attrs={"class": "form-control"})
        }

class LangForm(forms.ModelForm):
    level = forms.ChoiceField(widget=forms.Select(attrs={"class":"form-control"}), choices=LanguageCV.LEVEL)

    class Meta():
        model = LanguageCV
        fields = ['language', 'level']
        widgets = {
            'language': forms.TextInput(attrs={"class": "form-control"}),
            'level': forms.TextInput(attrs={"class": "form-control"}),
        }

class SkillForm(forms.ModelForm):
    class Meta():
        model = Skill
        fields = ['name']
        widgets = {
            'name': forms.Textarea(attrs={"class": "form-control"})
        }