'''from multiprocessing import context
from django.shortcuts import render
from visitantes.models import Visitante


def index(request):
    
    todos_visitantes = Visitante.objects.all()
    
    context = {
        "nome_pagina": "Inicio da dashboard",
        "todos_visitantes" : todos_visitantes,
    }
    
    return render(request, "index.html",context)
'''