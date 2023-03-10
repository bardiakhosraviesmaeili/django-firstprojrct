from django.shortcuts import render
from .models import Todo


def say_hello(request):
    return render(request, 'hello.html', context={'name': 'Bardia', 'last_name': 'khosravi esmaeili'})


def home(request):
    all=Todo.objects.all()
    return render(request, 'home.html', {'todos':all})
