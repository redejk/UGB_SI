from django.shortcuts import render
from .models import Discos
# Create your views here.
def list_discos(request):
    discos = Discos.objects.all()
    template_name = 'list_discos.html'
    context = {
        'discos' : discos
    }
    return render(request, template_name, context)