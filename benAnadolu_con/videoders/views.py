from django.views.generic.list import ListView
from videoders.models import *

class VideolarView(ListView):
    model = VideoDers
    template_name = "videoders.html"
    context_object_name = "videolar"
    paginate_by = 8