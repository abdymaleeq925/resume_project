from urllib import request
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from backend.apps.resumesite.forms import *
from django.urls import reverse_lazy
from .forms import EducationFormSet

def home(request):
    return render(request, 'index.html', {})

def service(request):
    return render(request, 'service.html', {})

def aboutus(request):
    return render(request, 'aboutus.html', {})


class CVShow(CreateView):
    form_class = ProfileForm
    template_name = "profile.html"
    success_url = reverse_lazy("education")
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CVShow, self).form_valid(form)


class EduShow(CreateView):
    form_class = EducationForm
    template_name = "education.html"
    success_url = reverse_lazy("experience")
    
    def get(self, *args, **kwargs):
        formset = EducationFormSet(queryset=Education.objects.none())
        return self.render_to_response({'education_formset': formset})
    
    def post(self,*args, **kwargs):
        formset = EducationFormSet(data=self.request.POST)

        if formset.is_valid():
            formset.save()
            return redirect(reverse_lazy("education"))
        return self.render_to_response({'education_formset': formset})
        
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EduShow, self).form_valid(form)

class XPShow(CreateView):
    form_class = XPForm
    template_name = "experience.html"
    success_url = reverse_lazy("skills")
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EduShow, self).form_valid(form)