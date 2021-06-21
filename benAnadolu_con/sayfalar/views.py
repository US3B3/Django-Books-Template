from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def hakkinda(request):
    return render(request, "hakkinda.html")

def dene(request):
    return render(request, "dene.html")