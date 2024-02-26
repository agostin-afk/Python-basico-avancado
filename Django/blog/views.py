from django.shortcuts import render
from django.http import HttpResponse

def blog(request):
    context = {
            'texto': 'Bem-vindo ao Blog',
            }
    return render(
        request,
        'blog/home.html',
        context
    )

def exemplo(request):
    context = {
            'texto': 'Bem-vindo ao Exemplo',
            'title': 'Pagina de Exemplo - ',
            }
    return render(
        request,
        'blog/exemplo.html',
        context
    )
