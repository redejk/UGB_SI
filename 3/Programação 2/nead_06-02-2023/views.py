from django.shortcuts import render
from django.http import HttpResponse

def novo(request):
    dados = 'André Ricardo Prazeres Rodrigues'
    html = f"""
    <html>
    <head>
        <title>Aula 2</title>
    <head>
    <body>
    <h1>Aula 2</h1>
    <p>{dados} é simplesmente uma simulação de texto da indústria tipográfica e de impressos, e vem sendo utilizado desde o século XVI, quando um impressor desconhecido pegou uma bandeja de tipos e os embaralhou para fazer um livro de modelos de tipos. Lorem Ipsum sobreviveu não só a cinco séculos, como também ao salto para a editoração eletrônica, permanecendo essencialmente inalterado. Se popularizou na década de 60, quando a Letraset lançou decalques contendo passagens de Lorem Ipsum, e mais recentemente quando passou a ser integrado a softwares de editoração eletrônica como Aldus PageMaker.</p>
    </body>
    </html>
    """
    return HttpResponse(html)

def index(request):
    dados = 'UGB, index'
    html = f"""
    <html>
    <head>
        <title>Aula 2</title>
    <head>
    <body>
    <h1>Aula 2</h1>
    <p>{dados} é simplesmente uma simulação de texto da indústria tipográfica e de impressos, e vem sendo utilizado desde o século XVI, quando um impressor desconhecido pegou uma bandeja de tipos e os embaralhou para fazer um livro de modelos de tipos. Lorem Ipsum sobreviveu não só a cinco séculos, como também ao salto para a editoração eletrônica, permanecendo essencialmente inalterado. Se popularizou na década de 60, quando a Letraset lançou decalques contendo passagens de Lorem Ipsum, e mais recentemente quando passou a ser integrado a softwares de editoração eletrônica como Aldus PageMaker.</p>
    </body>
    </html>
    """
    return HttpResponse(html)
