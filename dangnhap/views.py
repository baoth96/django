from django.shortcuts import render
from dangky.models import NguoiDung

# Create your views here.

def home(request):
    return render(request, 'dangky/home.html')

def dangnhap(request):
    return render(request, 'dangnhap.html')

def xuly_dangnhap(request):
    ten = request.GET.get('ten')
    mk = request.GET.get('matkhau')

    data = NguoiDung.objects.filter(ten_dang_nhap = ten, mat_khau = mk)

    if data.exists():
        return render(request, 'thanhcong.html')
    else:
        return render(request, 'thatbai.html')