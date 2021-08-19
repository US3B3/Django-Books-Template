from django.views.generic.list import ListView
from videolar.models import VideoDers

class VideolarListView(ListView):
    model = VideoDers
    template_name = 'videoders.html'
