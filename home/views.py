from django.shortcuts import render, redirect
from .models import Todo
from django.contrib import messages
from .forms import TodpCreateform


def say_hello(request):
    return render(request, 'hello.html', context={'name': 'Bardia', 'last_name': 'khosravi esmaeili'})


def home(request):
    all = Todo.objects.all()
    return render(request, 'home.html', {'todos': all})


def detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request, 'detail.html', {'todo': todo})


def delete(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    messages.success(request, "todo deleted successfuly", "success")
    return redirect('home')


def create(request):
    form = TodpCreateform
    return render(request, 'create.html', {'form': form})
