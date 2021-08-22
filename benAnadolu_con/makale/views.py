from django.shortcuts import render
from . models import Kategori, Makale
from django.core.paginator import Paginator

def blog_list(request):
    makaleler = Makale.objects.all().order_by('-tarih')
    basmakale = Makale.objects.all().filter(basMakale = 1).order_by('-tarih')
    talimakale = Makale.objects.all().filter(taliMakale = 1).order_by('-tarih')
    kategoriler = Kategori.objects.order_by('isim')[0:11].all()
    context = {
        'makaleler' : makaleler,
        'basmakale' : basmakale[0],
        'talimakale' : talimakale[0:2],
        'kategoriler' : kategoriler,
    }
    return render(request, "blog.html", context)

def makale_detay(request, kategori_slug, makale_slug):
    makale = Makale.objects.get(kategori__slug=kategori_slug, makale_slug = makale_slug)

    context = {
        'makale' : makale
    }

    return render(request, 'sayfa.html', context)

def makaleler(request):
    makaleler = Makale.objects.all().order_by('-tarih')
    paginator = Paginator(makaleler, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'makaleler.html', {'page_obj': page_obj})

def kategori_list(request):
    kategoriler = Kategori.objects.order_by('isim')[0:11].all()
    context = {
        'kategoriler' : kategoriler,
    }
    return render(request, "kategoriler.html", context)

def kategori_detay(request, kategori_isim):
    kategori_detay = Makale.objects.filter(kategori__isim=kategori_isim).all()
    kategori = kategori_isim

    context = {
        'kategori_detay' : kategori_detay,
        'kategori' : kategori,
    }

    return render(request, 'kategori.html', context)

def etiket_list(request):
    kategoriler = Kategori.objects.order_by('isim')[0:11].all()
    context = {
        'kategoriler' : kategoriler,
    }
    return render(request, "kategoriler.html", context)