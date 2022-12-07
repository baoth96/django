from django.contrib import admin
from django.urls import path
from truongphong import views

urlpatterns = [
    path('truongphong/', views.truongphong),
]