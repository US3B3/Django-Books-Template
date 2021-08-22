from django.urls import path
from videoders.views import *

urlpatterns = [
    path('', VideolarView.as_view(), name="videoders"),
]
