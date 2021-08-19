from django.urls import path
from videolar.views import VideolarListView

urlpatterns = [
    path('', VideolarListView.as_view(), name="videolar"),
]
