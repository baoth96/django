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

    data_role = NguoiDung.objects.filter(ten_dang_nhap = ten, mat_khau = mk).values('role')
    lst = list(data_role)
    a = lst[0]
    b = int(a.get("role"))

    if (b == 1):
        context = {
            'ten' : ten,
            'mk' : mk,
        }
        return render(request, 'nhanvien.html', context)

    elif (b == 2):
        # context = {
        #     'ten' : ten,
        #     'mk' : mk,
        # }
        print("truong phong")
        return render(request, 'truongphong.html')
       
    