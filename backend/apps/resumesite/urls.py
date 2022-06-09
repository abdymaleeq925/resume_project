from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('service/', service, name='service'),
    path('aboutus/', aboutus, name='aboutus')
]
