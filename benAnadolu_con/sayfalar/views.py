from makale.models import Makale, Kategori
from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name="index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['biyografiler'] = Makale.objects.filter(kategori__isim="Biyografi").all().order_by("tarih")[:4]
        context['makaleler'] = Makale.objects.exclude(kategori__isim="Biyografi").all().order_by("tarih")[:4]
        return context

class HakkındaView(TemplateView):
    template_name="hakkinda.html"

class BlogView(TemplateView):
    template_name="blog.html"

class VideoView(TemplateView):
    template_name="videoders.html"

class GaleriView(TemplateView):
    template_name="galeri.html"

class VitrinView(TemplateView):
    template_name="vitrin.html"

class BiyografiView(TemplateView):
    template_name="biyografi.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['biyografiler'] = Makale.objects.filter(kategori__isim="Biyografi").all().order_by("tarih")[:4]
        return context

class SayfaView(TemplateView):
    template_name="sayfa.html"
