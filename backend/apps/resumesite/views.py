from cmd import IDENTCHARS
from urllib import request
from xml.dom.minidom import Identified
from django.http import Http404
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView
from django.views.generic.edit import FormView
from backend.apps.resumesite.forms import *
from backend.apps.resumesite.models import *
from django.urls import reverse_lazy, reverse

def home(request):
    return render(request, 'index.html', {})

def service(request):
    return render(request, 'service.html', {})

def aboutus(request):
    return render(request, 'aboutus.html', {})

def nextpage(request):
    return render(request, 'expreience.html', {})

class MyResumes(ListView):
    model = CV
    template_name = "myresumes.html"

    def get_context_data(self, **kwargs):
        context = super(MyResumes, self).get_context_data(**kwargs)
        user_cv = self.request.user.id
        context['resumes'] = CV.objects.filter(user_id=user_cv)
        return context 
    

class ResumeTemplates(FormView):
    form_class = ResumeForm
    fields = ['name', 'template_image']
    template_name = "resumetemplates.html"
    success_url = reverse_lazy("profile")

    def form_valid(self, form):
        return super(ResumeTemplates, self).form_valid(form)

class CVShow(CreateView):
    form_class=ProfileForm
    template_name = "profile.html"
    success_url = reverse_lazy("education")
    
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return super().form_valid(form)

    def get_success_url(self):
        cv_id = self.object.pk
        return reverse_lazy("education", kwargs={"pk":cv_id})   

        
class EduShow(CreateView):
    template_name = "education.html"

    form_class = EducationForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        cv_id = self.kwargs.get('pk')
        try:
            cv=CV.objects.get(id=cv_id)
        except CV.DoesNotExist:
            raise Http404
        instance.resume = cv
        instance.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        educations = Education.objects.filter(resume__id=self.kwargs.get('pk'))
        context['educations'] = educations
        return context

    def get_success_url(self):
        cv_id = self.kwargs.get('pk')
        return reverse_lazy("education", kwargs={"pk":cv_id})    


def DelEduShow(request, pk):
    model = Education.objects.filter(id=pk)
    model.delete()
    return reverse_lazy("education", kwargs={"pk":35})


class XPShow(CreateView):
    form_class = XPForm
    template_name = "experience.html"
    
    
    def form_valid(self, form):
        instance = form.save(commit=False)
        cv_id = self.kwargs.get('pk')
        try:
            cv=CV.objects.get(id=cv_id)
        except CV.DoesNotExist:
            raise Http404
        instance.resume = cv
        instance.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        experiences = Experience.objects.filter(resume__id=self.kwargs.get('pk'))
        context['experiences'] = experiences
        return context

    def get_success_url(self):
        cv_id = self.kwargs.get('pk')
        return reverse_lazy("experience", kwargs={"pk":cv_id}) 


class SkillShow(CreateView):
    form_class = SkillForm
    template_name = "skills.html"

    def form_valid(self, form):
        instance = form.save(commit=False)
        cv_id = self.kwargs.get('pk')
        try:
            cv=CV.objects.get(id=cv_id)
        except CV.DoesNotExist:
            raise Http404
        instance.resume = cv
        instance.save()
        return super().form_valid(form)

    def get_success_url(self):
        cv_id = self.kwargs.get('pk')
        return reverse_lazy("language", kwargs={"pk":cv_id})


class LangShow(CreateView):
    form_class = LangForm
    template_name = "language.html"
    
    
    def form_valid(self, form):
        instance = form.save(commit=False)
        cv_id = self.kwargs.get('pk')
        try:
            cv=CV.objects.get(id=cv_id)
        except CV.DoesNotExist:
            raise Http404
        instance.resume = cv
        instance.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        languages = LanguageCV.objects.filter(resume__id=self.kwargs.get('pk'))
        context['languages'] = languages
        return context

    def get_success_url(self):
        cv_id = self.kwargs.get('pk')
        return reverse_lazy("resumetemplates", kwargs={"pk":cv_id}) 


class ResumeDetailView(UpdateView):
    model = CV
    fields = ['resume_name', 'first_name', 'last_name', 'photo', 'email', 'mobile', 'address', 'location', 'prof_summary']
    template_name_suffix = '_detail'
    template_name = "cv_detail.html"

class EducationDetailView(UpdateView):
    model = Education
    form_class = EducationForm
    template_name_suffix = "_detail"
    template_name = "cv_detail.html"

    def get_success_url(self):
        cv_id = self.kwargs.get('pk')
        return reverse_lazy("education", kwargs={"pk": 35})

class ExperienceDetailView(UpdateView):
    model = Experience
    form_class = XPForm
    template_name_suffix = "_detail"
    template_name = "cv_detail.html"

    def get_success_url(self):
        return super(ExperienceDetailView).get_success_url()

class SkillDetailView(UpdateView):
    model = Skill
    form_class = SkillForm
    template_name_suffix = "_detail"
    template_name = "cv_detail.html"

    def get_success_url(self):
        return super(SkillDetailView).get_success_url()

def export(request):
    return render(request, 'export.html', {})

def export_resume(request, self):
    cv_id = self.kwargs.get('pk')
