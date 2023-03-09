from django.shortcuts import render


def say_hello(request):
    return render(request, 'hello.html', context={'name': 'Bardia', 'last_name': 'khosravi esmaeili'})

def home(request):
    return render(request, 'home.html')
