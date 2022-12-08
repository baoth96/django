from django.shortcuts import render, get_object_or_404
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
        data = NguoiDung.objects.all()
        context = {
            'dsnd': data,
        }
        return render(request, 'truongphong.html', context)
       
def xuly_xoa(request, nguoidung_id):
    data = get_object_or_404(NguoiDung, pk = nguoidung_id)
    data.delete()
    danh_sach = NguoiDung.objects.all()
    context = {
        'dsnd': danh_sach,
    }
    return render(request, 'truongphong.html', context)
