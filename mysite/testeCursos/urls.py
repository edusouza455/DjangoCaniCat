from django.urls import path, include 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gato/', views.gato, name='gato'),
    path('lista/', views.lista, name='lista'),
]
