from django.shortcuts import render, HttpResponse
from django.views import View
from django.template import loader


def index(request, idade, nome=''):
    return HttpResponse(f'<h1>Minha primeira pagina django</h1>'
                        f'<h3>olá {nome} {idade} seja bem-vindo')


def soma(request, num1, num2):
    return HttpResponse(f'<h2> A soma da operação é {int(num1) + int(num2)}')


def sub(request, num1, num2):
    return HttpResponse(f'<h2> A subtração da operação é {int(num1) - int(num2)}')


def mult(request, num1, num2):
    return HttpResponse(f'<h2> A multiplicação da operação é {int(num1) * int(num2)}')


def div(request, num1, num2):
    return HttpResponse(f'<h2> A divisão da operação é {int(num1) / int(num2)}')


class IndexView(View):

    template_name = 'index.html'

    def get(self, request, nome):
        conteudo = loader.render_to_string(self.template_name, context={'nome': nome})
        return HttpResponse(conteudo)
