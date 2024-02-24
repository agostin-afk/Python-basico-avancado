from django.shortcuts import render
from django.http import HttpResponse

def blog(request):
    return render(request, 'blog/home.html')

def exemplo(request):
    return render(request, 'blog/exemplo.html')