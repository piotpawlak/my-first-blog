from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})


def strona_glowna(request):
    imie = "Piotr"
    nazwisko = "Pawlak"
    html = "<html><body>It is now %s.</body></html" % imie+nazwisko
    return HttpResponse(html)

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def strona_imion(request):
    imie = "Piotr"
    return render(request, 'blog/imie.html', {'toimie':imie})

def data(request):
    now = datetime.datetime.now()
    return render(request, 'blog/data.html', {'data':now})
