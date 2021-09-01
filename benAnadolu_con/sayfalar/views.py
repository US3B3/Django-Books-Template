from django.views.generic.edit import FormView
from makale.models import Makale
from django.views.generic import TemplateView
from videoders.models import VideoDers
from django.db.models import Q
from django.shortcuts import render
from django.core.paginator import Paginator
from . forms import İletisimFormu
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


class IndexView(SuccessMessageMixin, FormView):
    template_name="index.html"
    form_class = İletisimFormu
    success_url = "."
    success_message = 'Mesajınız İletilmiştir'

    def form_valid(self, form):
        form.save()
        return super(IndexView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['biyografiler'] = Makale.objects.filter(kategori__isim="Biyografi").all().order_by("tarih")[:4]
        context['makaleler'] = Makale.objects.exclude(kategori__isim="Biyografi").all().order_by("tarih")[:4]
        context['videolar'] = VideoDers.objects.all().order_by("tarih")
        return context

class HakkındaView(TemplateView):
    template_name="hakkinda.html"

class BlogView(TemplateView):
    template_name="blog.html"

class BiyografiView(TemplateView):
    template_name="biyografi.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['biyografiler'] = Makale.objects.filter(kategori__isim="Biyografi").all().order_by("tarih")[:4]
        return context

class SayfaView(TemplateView):
    template_name="sayfa.html"

def Arama(request):
    sonuclar = Makale.objects.filter(Q(isim__contains = request.GET['arama']) | Q(aciklama__contains = request.GET['arama']))

    paginator = Paginator(sonuclar,16)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'sonuclar.html', {'sonuclar': page_obj})

