from django.urls import path
from . import views

urlpatterns = [
    path('', views.makale_list, name="blog"),
    path('<slug:kategori_slug>/<str:makale_isim>', views.makale_detay, name="makale_detay"),
]
