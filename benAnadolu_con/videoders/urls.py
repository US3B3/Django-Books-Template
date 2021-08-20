from django.urls import path
from . import views

urlpatterns = [
    path('', views.VideolarView, name="kategori_liste"),
]
