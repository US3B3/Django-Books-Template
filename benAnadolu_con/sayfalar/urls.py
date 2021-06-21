from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('hakkinda/', views.hakkinda, name="hakkinda"),
    path('dene/', views.dene, name="dene"),
]
