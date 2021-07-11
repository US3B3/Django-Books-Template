from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('blog/', views.blog, name="blog"),
    path('videoders/', views.videoders, name="videoders"),
    path('galeri/', views.galeri, name="galeri"),
    path('vitrin/', views.vitrin, name="vitrin"),
    path('biyografi/', views.biyografi, name="biyografi"),
    path('hakkinda/', views.hakkinda, name="hakkinda"),
    path('sayfa/', views.sayfa, name="sayfa"),
    path('dene/', views.dene, name="dene"),
]
