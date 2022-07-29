from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def saludo(request):
    return HttpResponse('Holis testeando httpResponse')

def template(request):
    today = datetime.today().date
    context = {
        'name':'Emiliano',
        'last_name':'Anselmini',
        'date':today
    }
    return render(request, 'template.html', context=context)

def lista(request):
    context = {
        'lista':['Ruben','Nancy','Diego', 'Marta'],
    }
    return render(request, 'lista.html', context=context)