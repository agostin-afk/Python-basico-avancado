from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {
        'text': 'Ola Mundo',
    }
    return render(
        request, 
        'home/index.html',
        context
    )