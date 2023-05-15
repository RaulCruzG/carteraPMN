from django.urls import path
from . import views

urlpatterns = [
    path('', views.cartera_show, name='cartera'),
]