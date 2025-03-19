from django.shortcuts import render
from .models import Todo


# Create your views here.
def todo_list(requast):
    todos = Todo.objects.all()

    return render(requast, "todos/todo_list.html",  {"todos":todos});
