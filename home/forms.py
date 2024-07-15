from django import forms
from .models import Loai

class TheLoaiForm(forms.Form):
	TenLoai = forms.CharField(label='Tên thể loại', max_length=100)
	def clean_TenLoai(self):
		TenLoai = self.cleaned_data['TenLoai']
		try:
			Loai.objects.get(TenLoai=TenLoai)
		except Loai.DoesNotExist:
			return TenLoai
		raise forms.ValidationError('Tên loại đã tồn tại')
	def save(self):
		Loai.objects.create(TenLoai=self.cleaned_data['TenLoai'])