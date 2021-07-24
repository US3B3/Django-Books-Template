from django.shortcuts import render

def makale_list(request):
    return render(request, "blog.html")