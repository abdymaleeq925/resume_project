from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginView.as_view(),name='sign_in'),
    path('register/', UserRegistrationView.as_view(),name='signup'),
    path('register/done/', RegisterDoneView.as_view(), name="signup_done"),
    path('logout/', user_logout, name='logout')    
]
