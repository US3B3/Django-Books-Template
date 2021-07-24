from django.urls import path
from . import views

urlpatterns = [
    path('', views.makale_list, name="blog"),

]
