from django.shortcuts import render

from django.http import HttpResponse
def index(request):
    nome = 'Carlos'
    html = f"""
    <html>
    <head>
        <title>Aula 3</title>
    </head>
    <body>
        <h1>{nome}</h1>
    </body>

    </html>

    """
    return HttpResponse(html)
