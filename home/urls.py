from django.urls import path
from home import views

urlpatterns = [
    path('', views.homeIndex, name='homeIndex'),
]