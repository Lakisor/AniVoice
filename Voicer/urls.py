from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('registration/', registration, name='registration'),
    path('login/', user_login, name='login'),
    path("logout/", user_logout, name="logout"),
    path("user/<str:username>/", usercab, name='usercab'),
    path("animes/", anime_list, name='animes'),
    path("editusername/<str:username>/", editusername, name="editusername"),
    path("editpassword/", editpassword, name="editpass"),
    path("create_tour/", create_tour, name="create_tour"),
]
