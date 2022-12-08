from django.contrib import admin
from django.urls import path
from nhanvien import views

urlpatterns = [
    path('/nhanvien/<int:id>/', views.nhanvien),
    path('xuly_capnhat/<int:id>/', views.xuly_capnhat, name='xuly_capnhat'),
]