from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('UGB')

def nome(request):
    name = 'André Ricardo Prazeres Rodrigues'
    html = f'''
    <html>
    <head>
    <title>Aula 3</title>
    </head>
    <body>
    <h1>{name}</h1>
    </body>
    </html>
    '''
    return HttpResponse(html)