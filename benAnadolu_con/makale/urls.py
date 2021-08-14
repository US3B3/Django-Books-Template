from django.urls import path
from . import views

urlpatterns = [
    path('', views.makale_list, name="blog"),
    path('kategori/', views.kategori_list, name="kategori_liste"),
    path('kategori/<str:kategori_isim>', views.kategori_detay, name="kategori_detay"),
    path('<slug:kategori_slug>/<str:makale_isim>', views.makale_detay, name="makale_detay"),
]
