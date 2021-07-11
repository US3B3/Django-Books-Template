from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def hakkinda(request):
    return render(request, "hakkinda.html")

def blog(request):
    return render(request, "blog.html")

def videoders(request):
    return render(request, "videoders.html")

def galeri(request):
    return render(request, "galeri.html")

def vitrin(request):
    return render(request, "vitrin.html")

def biyografi(request):
    return render(request, "biyografi.html")

def sayfa(request):
    return render(request, "sayfa.html")

def dene(request):
    return render(request, "dene.html")