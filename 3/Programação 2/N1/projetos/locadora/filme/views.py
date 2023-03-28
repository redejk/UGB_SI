from django.shortcuts import render
from .models import Filmes
from django.http import HttpResponse
# Create your views here.

def base(request):
    filmes = Filmes.objects.all()
    template_name = 'base.html'
    context = {
        'filmes': filmes
    }
    return render(request, template_name, context)

def filme_list(request):
    filmes = Filmes.objects.all()
    template_name = 'filme_list.html'
    context = {
        'filmes' : filmes
    }
    return render(request, template_name, context)

def filme_new(request):
    pass

def filme_delete(request):
    pass

def filme_edit(request):
    pass