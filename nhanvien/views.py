from django.shortcuts import render, get_object_or_404
from dangky.models import NguoiDung

# Create your views here.

def home(request):
    return render(request, 'dangky/home.html')

def nhanvien(request, nguoidung_id):
    nguoi_dung = get_object_or_404(NguoiDung, pk = nguoidung_id)
    return render(request, 'nhanvien.html', {'nd': nguoi_dung})

def xuly_capnhat(request, nguoidung_id):
    nguoi_dung = get_object_or_404(NguoiDung, pk = nguoidung_id)
    return render(request, 'nhanvien.html', {'nd': nguoi_dung})