from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username=None, password=None, **extra_fields):
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(username, password, **extra_fields)

class User(AbstractUser):
    username = models.CharField("Пользователь", max_length=50, unique=True)
    email = models.EmailField("Электронная почта", unique=True)
    prof_pic = models.ImageField("Фото", upload_to="user/images/", null=True, blank=True)
    phone = models.CharField("Номер телефона", null=True, max_length=9)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = UserManager()
