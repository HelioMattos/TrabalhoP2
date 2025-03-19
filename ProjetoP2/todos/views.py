from django.shortcuts import render
from .models import Todo


# Create your views here.
from django.views.generic import ListView,  CreateView

class TodoListView(ListView):
    model = Todo

class TodoCreateView(CreateView):
 model = Todo
 fields = ["title", "deadline"]


def todo_list(requast):
    todos = Todo.objects.all()

    return render(requast, "todos/todo_list.html",  {"todos":todos});
