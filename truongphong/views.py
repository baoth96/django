from django.shortcuts import render, get_object_or_404
from dangky.models import NguoiDung

# Create your views here.

def home(request):
    return render(request, 'dangky/home.html')

def truongphong(request):
    return render(request, 'truongphong.html')

def cap_nhat_nhan_vien(request,nguoidung_id):
    nguoi_dung = get_object_or_404(NguoiDung, pk = nguoidung_id)
    return render(request, 'capnhatnhanvien.html', {'nd': nguoi_dung})

def xu_ly_cap_nhat(request):
    id_nguoidung = request.GET.get('id_nguoidung')
    ten = request.GET.get('ten')
    mail = request.GET.get('mail')
    mk = request.GET.get('matkhau')

    NguoiDung.objects.filter(id = id_nguoidung).update(
        ten_dang_nhap = ten,
        email = mail,
        mat_khau = mk,
    )

    data = NguoiDung.objects.filter(ten_dang_nhap = ten, mat_khau = mk)

    danh_sach = NguoiDung.objects.all()
    context = {
        'dsnd': danh_sach,
    }
    return render(request, 'truongphong.html', context)

def tim_kiem(request):

    ten = request.GET.get('ten')

    data = NguoiDung.objects.filter(ten_dang_nhap__icontains = ten)

    context = {
        'dsnd': data,
    }
    return render(request, 'truongphong.html', context)