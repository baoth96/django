from django.contrib import admin
from django.urls import path
from truongphong import views
from nhanvien.views import nhanvien
urlpatterns = [
    path('truongphong/', views.truongphong),
    path('<int:nguoidung_id>/', views.cap_nhat_nhan_vien, name='cap_nhat_nhan_vien'),
    path('capnhat/',views.xu_ly_cap_nhat, name='xu_ly_cap_nhat'),
    
]