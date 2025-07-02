from django.shortcuts import render
from django.http import HttpResponse
from .models import Produto

def ver_produto(request):
    '''return HttpResponse('estou no ver')'''
    if request.method == "GET":
        return render(request, 'ver_produto.htm')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        quantidade = request.POST.get('quantidade')
        
        produto = Produto(nome=nome, quantidade=quantidade)
        
        produto.save()
        
        return HttpResponse('Produto Cadastrado com Sucesso!')
    

def inserir_produto(request):
    return HttpResponse('Estou no inserir')