from django.views.generic.list import ListView
from vitrin.models import *
from sayfalar.models import Ayarlar

class VitrinView(ListView):
    model = Vitrin
    template_name = "vitrin.html"
    context_object_name = "vitrin"
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ayarlar'] = Ayarlar.objects.get()
        return context