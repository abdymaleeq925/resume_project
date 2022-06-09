from django import forms

from .models import User

from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(
        label = "Пользователь",
        widget = forms.TextInput(attrs={"class":"form-control"})
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "type":"password",
                "autocomplete":"off",
                "placeholder":"Пароль"
                }
            )
    )    

class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label = "Пароль",
        widget = forms.PasswordInput(attrs={"class":"form-control"})
    )
    password2 = forms.CharField(
        label = "Повторите пароль",
        widget = forms.PasswordInput(attrs={"class":"form-control"})
    )

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'phone',
            'email'
        ]
        widgets = {
            "username": forms.TextInput(attrs={"class":"form-control"}),
            "first_name": forms.TextInput(attrs={"class":"form-control"}),
            "last_name": forms.TextInput(attrs={"class":"form-control"}),
            "phone": forms.TextInput(attrs={"class":"form-control"}),
            "email": forms.EmailInput(attrs={"class":"form-control"})
        }
