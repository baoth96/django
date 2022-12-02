from django.contrib import admin
from django.urls import path
from nhanvien import views

urlpatterns = [
    path('/nhanvien/<int:id>/', views.nhanvien),
    # path('edit_nhanvien/', views.edit_nhanvien, name='edit_nhanvien'),
]