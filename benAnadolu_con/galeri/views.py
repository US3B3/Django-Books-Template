from django.views.generic.list import ListView
from galeri.models import *
from sayfalar.models import Ayarlar

class GaleriView(ListView):
    model = Galeri
    template_name = "galeri.html"
    context_object_name = "galeri"
    paginate_by = 12
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['galeri'] = Galeri.objects.filter(erisim=True)
        context['ayarlar'] = Ayarlar.objects.get()
        return context