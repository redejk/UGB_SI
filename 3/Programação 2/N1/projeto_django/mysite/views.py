from django.http import HttpResponse
def index(request):
    html = """
    <html>
    <head>
        <title>Aula 3</title>
    </head>
    <body>
        <h1>Carlos</h1>
    </body>

    </html>

    """
    return HttpResponse(html)