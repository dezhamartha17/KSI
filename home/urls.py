from django.urls import path, re_path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    re_path(r'^articles/(?P<year>[0-9]{4})/$', views.articles, name='dinamis'),
]