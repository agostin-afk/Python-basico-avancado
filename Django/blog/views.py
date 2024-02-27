from django.shortcuts import render
from django.http import HttpResponse
from blog.data import posts
def blog(request):
    context = {
            'texto': 'Bem-vindo ao Blog',
            'posts': posts
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
def post(request, post_id):
    found_post = None
    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break
    context = {
        'post': found_post
    }

    return render(
        request,
        'blog/post.html',
        context
    )
