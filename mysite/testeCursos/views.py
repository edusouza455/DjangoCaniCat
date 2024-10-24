from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db import models
from .forms import ListaForm
from .models import Lista

def index(request):
    return render(request, 'testeCursos/index.html')

def gato(request):
    return render(request, 'testeCursos/gato.html')


def lista(request):
    return render(request, 'testeCursos/lista.html')

