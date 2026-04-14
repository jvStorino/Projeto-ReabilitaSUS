from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContatoForm


def home(request):
    return render(request, 'home.html', {'page_title': 'ReabilitaSUS - Home'})


def apresentacao(request):
    return render(request, 'apresentacao.html', {'page_title': 'Apresentação - ReabilitaSUS'})


def resumo(request):
    return render(request, 'resumo.html', {'page_title': 'Resumo do Projeto'})


def sobre(request):
    return render(request, 'sobre.html', {'page_title': 'Sobre ReabilitaSUS'})


def rcpd(request):
    return render(request, 'rcpd.html', {'page_title': 'RCPD - ReabilitaSUS'})


def normativa(request):
    return render(request, 'normativa.html', {'page_title': 'Base Normativa'})


def funcionalidades(request):
    return render(request, 'funcionalidades.html', {'page_title': 'Funcionalidades'})


def exercicios(request):
    return render(request, 'exercicios.html', {'page_title': 'Exercícios Guiados'})


def exercicios_iniciante(request):
    return render(request, 'exercicios_iniciante.html', {'page_title': 'Exercícios Iniciante'})


def exercicios_medio(request):
    return render(request, 'exercicios_medio.html', {'page_title': 'Exercícios Médio'})


def exercicios_avancado(request):
    return render(request, 'exercicios_avancado.html', {'page_title': 'Exercícios Avançado'})


def acessibilidade(request):
    return render(request, 'acessibilidade.html', {'page_title': 'Acessibilidade'})


def lembretes(request):
    return render(request, 'lembretes.html', {'page_title': 'Lembretes'})


def acompanhamento(request):
    return render(request, 'acompanhamento.html', {'page_title': 'Acompanhamento Remoto'})


def publico_alvo(request):
    return render(request, 'publico_alvo.html', {'page_title': 'Público-Alvo'})


def deficiencias(request):
    return render(request, 'deficiencias.html', {'page_title': 'Tipos de Deficiência'})


def cuidadores(request):
    return render(request, 'cuidadores.html', {'page_title': 'Cuidadores'})


def beneficios(request):
    return render(request, 'beneficios.html', {'page_title': 'Benefícios'})


def impactos(request):
    return render(request, 'impactos.html', {'page_title': 'Impactos Positivos'})


def contato(request):
    form = ContatoForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Mensagem enviada com sucesso! Entraremos em contato em breve.')
            return redirect('contato')
    return render(request, 'contato.html', {'page_title': 'Contato', 'form': form})
