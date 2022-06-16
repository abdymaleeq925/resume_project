from django import forms
from .models import *
from django.forms import modelformset_factory

class ProfileForm(forms.ModelForm):
    class Meta():
        model = CV
        fields = ['first_name', 'last_name', 'photo', 'email', 'mobile', 'address', 'location', 'prof_summary']
        widgets = {
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
    class Meta():
        model = Education
        fields = ['school', 'degree', 'fieldstudy', 'start_date', 'end_date']
        widgets = {
            'school': forms.TextInput(attrs={"class": "form-control"}),
            'degree': forms.TextInput(attrs={"class": "form-control"}),
            'fieldstudy': forms.TextInput(attrs={"class": "form-control"}),
            'start_date': forms.DateInput(attrs={"class": "form-control"}),
            'end_date': forms.DateInput(attrs={"class": "form-control"})
        }

EducationFormSet = forms.modelformset_factory(Education, fields=('school', 'degree', 'fieldstudy', 'start_date', 'end_date'), extra=1)


class XPForm(forms.ModelForm):
    class Meta():
        model = Experience
        fields = ['job_title', 'company_name', 'job_location', 'start_date', 'end_date', 'job_description']
        widgets = {
            'job_title': forms.TextInput(attrs={"class": "form-control"}),
            'company_name': forms.TextInput(attrs={"class": "form-control"}),
            'job_location': forms.TextInput(attrs={"class": "form-control"}),
            'start_date': forms.DateInput(attrs={"class": "form-control"}),
            'end_date': forms.DateInput(attrs={"class": "form-control"}),
            'job_description': forms.Textarea(attrs={"class": "form-control"})
        }

class LangForm(forms.ModelForm):
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