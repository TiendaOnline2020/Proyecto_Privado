from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import *
from django.contrib.auth.views import LoginView

from django.contrib.auth.decorators import login_required
app_name = 'core'
urlpatterns = [
    path('', home, name='casa'),
]
