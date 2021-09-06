from django.db import models
from django.shortcuts import render
from . models import Etiket, Kategori, Makale
from django.core.paginator import Paginator
from sayfalar.models import Ayarlar

def blog_list(request):
    makaleler = Makale.objects.all().order_by('-tarih')
    basmakale = Makale.objects.all().filter(basMakale = 1).order_by('-tarih')
    talimakale = Makale.objects.all().filter(taliMakale = 1).order_by('-tarih')
    kategoriler = Kategori.objects.order_by('isim')[0:11].all()
    ayarlar = Ayarlar.objects.get()

    context = {
        'makaleler' : makaleler,
        'basmakale' : basmakale[0],
        'talimakale' : talimakale[0:2],
        'kategoriler' : kategoriler,
        'ayarlar' : ayarlar,
    }
    return render(request, "blog.html", context)

def makale_detay(request, kategori_slug, makale_slug):
    makale = Makale.objects.get(kategori__slug=kategori_slug, makale_slug = makale_slug)
    ayarlar = Ayarlar.objects.get()
    context = {
        'makale' : makale,
        'ayarlar' : ayarlar,
    }

    return render(request, 'sayfa.html', context)

def makaleler(request):
    makaleler = Makale.objects.all().order_by('-tarih')
    ayarlar = Ayarlar.objects.get()
    paginator = Paginator(makaleler, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'makaleler.html', {'page_obj': page_obj, 'ayarlar': ayarlar})

def kategori_list(request):
    kategoriler = Kategori.objects.order_by('isim')[0:11].all()
    ayarlar = Ayarlar.objects.get()
    paginator = Paginator(kategoriler, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'kategoriler.html', {'kategoriler': page_obj, 'ayarlar':ayarlar})

def kategori_detay(request, kategori_isim):
    kategori_detay = Makale.objects.filter(kategori__isim=kategori_isim).all()
    kategori = kategori_isim
    ayarlar = Ayarlar.objects.get()
    paginator = Paginator(kategori_detay, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'kategori.html', {'kategori_detay' : kategori_detay,'kategori' : kategori,'ayarlar': ayarlar, 'page_obj':page_obj})

def etiket_list(request):
    kategoriler = Kategori.objects.order_by('isim')[0:11].all()
    ayarlar = Ayarlar.objects.get()
    context = {
        'kategoriler' : kategoriler,
        'ayarlar' : ayarlar,
    }
    return render(request, "kategoriler.html", context)