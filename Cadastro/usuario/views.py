
from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
from .models import Usuario

def cadastro(request):
    return HttpResponse('Você está na página de cadastro')


def login(request):
    status = request.GET.get('status')
    return render(request, 'login/login.html', {'status':status})

def home(request):
    return HttpResponse('Você está na home')

def salvar(request):
    nome = request.Post.get('nome')
    sobrenome = request.Post.get('sobrenome')
    idade= request.Post.get('idade')
    try:

        usuario = Usuario(
            nome = nome,
            sobrenome = sobrenome,
            idade = idade
        )
        usuario.save()
        return redirect('/usuario/login?status=1')
    except:
        return redirect('/usuario/login?status=2')

