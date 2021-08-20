from django.shortcuts import render
from videoders.models import VideoDers
from makale.models import Makale

def VideolarView(request):
    videolar = VideoDers.objects.all().order_by("tarih")
    anan = Makale.objects.all()

    context = {
        'videolar' : videolar,
        'anan' : anan
    }

    return render(request, 'videoders.html', context)

"""
class VideolarView(TemplateView):
    template_name = "videoders.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['videolar'] = VideoDers.objects.all().order_by("tarih")
        return context
"""