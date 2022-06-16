from django.urls import path
from .views import *
from .models import *

urlpatterns = [
    path('', home, name='home'),
    path('service/', service, name='service'),
    path('aboutus/', aboutus, name='aboutus'),
    path('profile/', CVShow.as_view(), name='profile'),
    path('education/',EduShow.as_view(), name='education'),
    path('experience/',XPShow.as_view(), name='experience'),
    # path('skills/',CVShow.as_view(), name='skills'),
    # path('language/',CVShow.as_view(), name='language')
]
