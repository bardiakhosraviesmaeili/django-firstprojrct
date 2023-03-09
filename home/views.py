from django.shortcuts import render


def say_hello(request):
    return render(request, 'hello.html')


def home(request):
    return render(request, 'home.html')
