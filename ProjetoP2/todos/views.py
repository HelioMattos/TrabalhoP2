from django.shortcuts import render


# Create your views here.
def todo_list(requast):
    nome = "Helio Mattos"
    alunos = ['1: Karina', '2: Yuri', '3: Douglas']

    return render(requast, "todos/todo_list.html",  {"nome": nome, "lista_alunos": alunos});
