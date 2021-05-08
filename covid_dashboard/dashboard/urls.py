"""Defines URL patterns for dashboard."""
from django.urls import path

from . import views

app_name = 'dashboard'

urlpatterns = [
    # Home page
    path('', views.index, name='index')
]