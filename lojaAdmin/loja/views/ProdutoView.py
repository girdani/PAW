from django.http import HttpResponse

def list_produto_view(request, id=None):
    return HttpResponse(f'<h1>Produto de id {id}!</h1>')