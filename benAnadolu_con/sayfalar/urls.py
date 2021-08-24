from django.urls import path
from sayfalar.views import *

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('biyografi/', BiyografiView.as_view(), name="biyografi"),
    path('hakkinda/', HakkındaView.as_view(), name="hakkinda"),
    path('sayfa/', SayfaView.as_view(), name="sayfa"),
    path('arama/', Arama, name="arama"),
    
]
