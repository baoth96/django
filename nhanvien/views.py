from django.shortcuts import render
from dangky.models import NguoiDung

# Create your views here.

def home(request):
    return render(request, 'dangky/home.html')

def nhanvien(request):
    return render(request, 'nhanvien.html')

