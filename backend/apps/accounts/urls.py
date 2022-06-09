from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginView.as_view(),name='signin'),
    path('signup/', UserRegistrationView.as_view(),name='signup'),
    path('signup/done/', RegisterDoneView.as_view(), name="signup_done"),
    path('logout/', user_logout, name='logout')    
]
