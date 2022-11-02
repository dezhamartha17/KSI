
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homeIndex(request):
    return render(request, 'index.html')

def articles(request,year):
    year = year
    str = year
    return HttpResponse(year)
