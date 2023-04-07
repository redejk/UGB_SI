from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Filmes, Generos
from .forms import FilmesForm, GenerosForm
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

def genero_list(request):
    generos = Generos.objects.all()
    template_name = 'genero_list.html'
    context = {
        'generos' : generos
    }
    return render(request, template_name, context)

def filme_new(request):
    if request.method == 'POST':
        form = FilmesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('filme_list')
    else:
        template_name = 'filme_new.html'
        context = {
            'form': FilmesForm()
        }
        return render(request, template_name, context)
    
def genero_new(request):
    if request.method == 'POST':
        form = GenerosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('genero_list')
    else:
        template_name = 'genero_new.html'
        context = {
            'form': GenerosForm()
        }
        return render(request, template_name, context)

def filme_edit(request, chave_primaria_filme):
    filme = Filmes.objects.get(id=chave_primaria_filme)
    if request.method == 'POST':
        form = FilmesForm(request.POST, instance=filme)
        if form.is_valid():
            form.save()
            return redirect('filme_list')
    else:
        template_name = 'filme_edit.html'
        context = {
            'form': FilmesForm(instance=filme),
            'chave_primaria_filme': chave_primaria_filme
        }
        return render(request, template_name, context)
    
def genero_edit(request, chave_primaria_genero):
    genero = Generos.objects.get(id=chave_primaria_genero)
    if request.method == 'POST':
        form = GenerosForm(request.POST, instance=genero)
        if form.is_valid():
            form.save()
            return redirect('genero_list')
    else:
        template_name = 'genero_edit.html'
        context = {
            'form': GenerosForm(instance=genero),
            'chave_primaria_genero': chave_primaria_genero
        }
        return render(request, template_name, context)

def filme_delete(request, chave_primaria_filme):
    filme = Filmes.objects.get(id=chave_primaria_filme)
    filme.delete()
    return redirect('filme_list')

def genero_delete(request, chave_primaria_genero):
    genero = Generos.objects.get(id=chave_primaria_genero)
    genero.delete()
    return redirect('genero_list')