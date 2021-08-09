from django.shortcuts import render
from . models import Makale

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