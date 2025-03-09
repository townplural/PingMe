from django.urls import path

from .views import *

app_name = "user"

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register_user'),
    path('profile/',  ProfileUser.as_view(), name='profile_user'),
    path('profile/edit/', EditUser.as_view(), name='edit_user'),
    path('login/', LoginUser.as_view(), name='login_user')
    
]
