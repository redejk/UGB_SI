from django.shortcuts import render
from .models import Pessoas
from django.http import HttpResponse

# def index(request):
#     nome = 'Carlos'
#     html = f"""
#     <html>
#     <head>
#         <title>Aula 3</title>
#     </head>
#     <body>
#         <h1>{nome}</h1>
#     </body>

#     </html>

#     """
#     return HttpResponse(html)

def index(request):
    pessoas = Pessoas.objects.all()
    template_name = 'index.html'
    context = {
        'pessoas': pessoas
    }
    return render(request, template_name, context)