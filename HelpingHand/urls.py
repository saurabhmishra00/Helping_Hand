from operator import index
from pathlib import Path

from django import views
from django.urls import path

from src.settings import TEMPLATES
 
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('Logged_in/',views.Logged_in,name='Logged_in'),
    path('registered/',views.registered,name='registered'),
    path('profile/',views.profile,name='profile')

]
