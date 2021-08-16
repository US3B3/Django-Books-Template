from django.urls import path
from sayfalar.views import *

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('videoders/', VideoView.as_view(), name="videoders"),
    path('galeri/', GaleriView.as_view(), name="galeri"),
    path('vitrin/', VitrinView.as_view(), name="vitrin"),
    path('biyografi/', BiyografiView.as_view(), name="biyografi"),
    path('hakkinda/', HakkındaView.as_view(), name="hakkinda"),
    path('sayfa/', SayfaView.as_view(), name="sayfa"),
]
