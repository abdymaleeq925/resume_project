from django.contrib import admin
from .models import *

@admin.register(ResumeTemplate)
class User(admin.ModelAdmin):
    list_display = (
        'id',
        'name', 
        )
    list_filter = [
        "name"
    ]
    search_fields = [
        "name"
    ]