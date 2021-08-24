from django.views.generic.list import ListView
from vitrin.models import *

class VitrinView(ListView):
    model = Vitrin
    template_name = "vitrin.html"
    context_object_name = "vitrin"
    paginate_by = 12