from django.shortcuts import render
from django.http import HttpResponse
from .models import Loai, SanPham
from .forms import TheLoaiForm
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
	return render(request, 'page/TrangChu.html')

def list(request):
	data = {
		'DM_loai': Loai.objects.all(),
	}
	return render(request, 'page/DSLoai.html', data)

def list1(request):
	data = {
		'DM_sp': SanPham.objects.all(),
	}
	return render(request, 'page/HienThiDSSP.html', data)

def list2(request):
	data = {
		'DM_SP': SanPham.objects.all(),
	}
	return render(request, 'page/HienThiSP.html', data)

def themloai(request):
	form = TheLoaiForm()
	if request.method == 'POST':
		form = TheLoaiForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/home/')
	return render(request, 'page/ThemLoai.html', {'form':form})

def dk(request):
	return render(request, 'page/DangKy.html')

def dn(request):
	return render(request, 'page/DangNhap.html')