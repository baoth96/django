from django.shortcuts import render, get_object_or_404
from dangky.models import NguoiDung

# Create your views here.

def home(request):
    return render(request, 'dangky/home.html')

def nhanvien(request, nguoidung_id):
    nguoi_dung = get_object_or_404(NguoiDung, pk = nguoidung_id)
    return render(request, 'nhanvien.html', {'nd': nguoi_dung})

# def xuly_capnhat(request):
#     # id_nguoidung = request.GET.get('id_nguoidung')
#     # ten = request.GET.get('ten')
#     # mail = request.GET.get('mail')
#     # mk = request.GET.get('matkhau')

#     # NguoiDung.objects.filter(id = id_nguoidung).update(
#     #     ten_dang_nhap = ten,
#     #     email = mail,
#     #     mat_khau = mk,
#     # )

    
#     return render(request, 'thanhcong.html')