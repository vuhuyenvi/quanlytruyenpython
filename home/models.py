from django.db import models

# Create your models here.
class Loai(models.Model):
	TenLoai = models.CharField(max_length=100)

class SanPham(models.Model):
    TenSP = models.CharField(max_length=100)
    DonGia = models.DecimalField(max_digits=10, decimal_places=2)
    HinhAnh = models.ImageField(upload_to='', blank=True, null=True)
    MoTa = models.CharField(max_length=500)
    ML_id = models.ForeignKey('Loai', on_delete=models.CASCADE)