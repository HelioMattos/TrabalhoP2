from django.shortcuts import render
from .models import Todo


# Create your views here.
from django.views.generic import ListView,  CreateView
from django.urls import reverse_lazy

class TodoListView(ListView):
    model = Todo;

class TodoCreateView(CreateView):
 model = Todo;
 fields = ["title", "deadline"]
 success_url = reverse_lazy("todo_list");


def todo_list(requast):
    todos = Todo.objects.all()

    return render(requast, "todos/todo_list.html",  {"todos":todos});
