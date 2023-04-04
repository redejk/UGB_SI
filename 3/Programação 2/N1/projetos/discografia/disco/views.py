from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Discos
from .forms import DiscosForm
# Create your views here.
def list_disco(request):
    discos = Discos.objects.all()
    template_name = 'list_disco.html'
    context = {
        'discos' : discos
    }
    return render(request, template_name, context)

def new_disco(request):
    print('O método é: ', request.method)
    if request.method == 'POST':
        form = DiscosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_disco')
    else:
        template_name = 'new_disco.html'
        context = {
            'form': DiscosForm()
        }
        return render(request, template_name, context)

def update_disco(request, pk):
    disco = Discos.objects.get(id=pk)
    if request.method == 'POST':
        form = DiscosForm(request.POST, instance=disco)
        if form.is_valid():
            form.save()
            return redirect('list_disco')
    else:
        template_name = 'update_disco.html'
        context = {
            'form': DiscosForm(instance=disco),
            'pk': pk
        }
        return render(request, template_name, context)

def delete_disco(request, pk):
    disco = Discos.objects.get(id=pk)
    disco.delete()
    return redirect('list_disco')
