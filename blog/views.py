from django.http import HttpResponse
import datetime
from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

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
