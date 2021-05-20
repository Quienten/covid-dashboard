"""Defines URL patterns for dashboard."""
from django.urls import path

from . import views

app_name = 'dashboard'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('about', views.page, name='about'),
    path('faq', views.page, name='faq'),
    path('contact', views.page, name='contact')
]