from django.shortcuts import render
from django.http import HttpResponse


# Initial Page
def page_web(request):
    return render(request, 'index.html', {'nome': 'Wescley'})


# Contato  Page
def contato(request):
    return render(request, 'contato.html')
