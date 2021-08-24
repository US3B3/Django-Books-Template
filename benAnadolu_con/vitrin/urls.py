from django.urls import path
from vitrin.views import *

urlpatterns = [
    path('', VitrinView.as_view(), name="vitrin"),
]