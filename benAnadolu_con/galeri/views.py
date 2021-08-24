from django.views.generic.list import ListView
from galeri.models import *

class GaleriView(ListView):
    model = Galeri
    template_name = "galeri.html"
    context_object_name = "galeri"
    paginate_by = 12