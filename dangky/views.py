from django.shortcuts import render
from django.http import HttpResponse
from dangky.models import NguoiDung

# Create your views here.

def home(request):
    return render(request, 'dangky/home.html')

def dangky(request):
    return render(request, 'dangky/dangky.html')

def xuly_dangky(request):
    ten = request.GET.get('tenDangNhap')
    mail = request.GET.get('email')
    mk = request.GET.get('matkhau')
    rol = request.GET.get('role')
    if (len(ten) < 5):
        return render(request, 'loi.html')
    else:
        data = NguoiDung(
            ten_dang_nhap = ten,
            email = mail,
            mat_khau = mk,
            role = rol,
        )
        data.save()
        return render(request, 'dangnhap.html')
    
    