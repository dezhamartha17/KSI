
from django.shortcuts import render
from django.http import HttpResponse


from .models import Post

# Create your views here.
def index(request):
    db = Post.objects.all()
    context = {
        'title' : 'testing view data',
        'body' : 'waduh',
        'post' : db,
        
    }
    return render(request, 'index.html', context)

def articles(request,year):
    year = year
    str = year
    return HttpResponse(year)

def blog(request):
    db = Post.objects.all()
    context = {
        'title' : 'testing view data',
        'body' : 'waduh',
        'post' : db,
        
    }
    return render(request, 'blog.html', context)