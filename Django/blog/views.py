from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, Http404
from blog.data import posts
from typing import Any
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
def post(request: HttpRequest, post_id: int):
    found_post: dict[str, Any] | None = None
    
    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break
    if found_post is None:
        raise Http404("Post not found")
    context = {
        'post': found_post,
        'title': found_post['title'] + '-',
    }

    return render(
        request,
        'blog/post.html',
        context
    )
