from django.contrib import admin
from django.urls import path
from dangnhap import views

urlpatterns = [
    path('', views.dangnhap),
    path('xuly_dangnhap/', views.xuly_dangnhap, name='xuly_dangnhap'),
    path('xoa/<int:nguoidung_id>', views.xuly_xoa, name='xuly_xoa'), 
]
