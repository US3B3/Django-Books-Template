from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name="blog"),
    path('makale/', views.makaleler, name="makaleler"),
    path('kategori/', views.kategori_list, name="kategori_liste"),
    path('kategori/<str:kategori_isim>', views.kategori_detay, name="kategori_detay"),
    path('<slug:kategori_slug>/<slug:makale_slug>', views.makale_detay, name="makale_detay"),
]
