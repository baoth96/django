from django.shortcuts import render
from django.http import HttpResponse
from dangky.models import NguoiDung
from django.core.mail import send_mail

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

        #Send email
        send_mail(
            'Chuc Mung',
            'Ban da dang ky thanh cong!',
            'vipronbk@gmail.com',
            [mail, 'techguyinfo@gmail.com'],
            fail_silently=False
        )

        return render(request, 'dangnhap.html')
    
    