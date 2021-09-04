from django.views.generic.list import ListView
from videoders.models import *
from sayfalar.models import Ayarlar

class VideolarView(ListView):
    model = VideoDers
    template_name = "videoders.html"
    context_object_name = "videolar"
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ayarlar'] = Ayarlar.objects.get()
        return context