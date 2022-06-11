from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import FormView, CreateView, TemplateView
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy

from .forms import *

class LoginView(FormView):
    template_name = "login.html"
    form_class = LoginForm

    def form_valid(self, form):
        data = form.cleaned_data
        username = data['username']
        password = data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return redirect("home")
            else:
                return HttpResponse("Ваш аккаунт неактивен")
        return HttpResponse("Такого пользователя не существует")

class UserRegistrationView(CreateView):
    template_name = "signup.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy('signup_done')


class RegisterDoneView(TemplateView):
    template_name = "signup_done.html"



def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('home')