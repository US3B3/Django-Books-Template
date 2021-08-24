from django.urls import path
from galeri.views import *

urlpatterns = [
    path('', GaleriView.as_view(), name="galeri"),
]