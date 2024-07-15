from django.urls import path
from . import views # call to url_shortener/views.py
urlpatterns = [
	path('', views.index, name='index'),
	path('dstheloai', views.list, name='dstheloai'),
	path('hienthidssp', views.list1, name='hienthidssp'),
	path('hienthisp', views.list2, name='hienthisp'),
	path('themloai', views.themloai, name='themloai'),
	path('dk', views.dk, name='dk'),
	path('dn', views.dn, name='dn'),
]