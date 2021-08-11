from django.shortcuts import render
from . models import Kategori, Makale

def makale_list(request):
    makaleler = Makale.objects.all().order_by('-tarih')
    basmakale = Makale.objects.all().filter(basMakale = 1).order_by('-tarih')
    talimakale = Makale.objects.all().filter(taliMakale = 1).order_by('-tarih')
    context = {
        'makaleler' : makaleler,
        'basmakale' : basmakale[0],
        'talimakale' : talimakale[0:2]
    }
    return render(request, "blog.html", context)

def makale_detay(request, kategori_slug, makale_isim):
    makale = Makale.objects.get(kategori__slug=kategori_slug, isim = makale_isim)

    context = {
        'makale' : makale
    }

    return render(request, 'sayfa.html', context)