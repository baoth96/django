from django.contrib import admin
from django.urls import path
from nhanvien import views

urlpatterns = [
    path('/nhanvien/<int:id>/', views.nhanvien, name="nhanvien"),
    path('cap_nhat_nv/', views.cap_nhat_nhan_vien, name='cap_nhat_nhan_vien'),
]