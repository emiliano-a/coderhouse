from django.shortcuts import render
from personas.models import Persona
# Create your views here.

def create_persona(request):
    new_persona = Persona.objects.create(nombre = 'Nancy Susana', apellido = 'Pellegrino', edad = 64, fecha_nacimiento = '1958-03-24')
    context = {
        'new_persona' : new_persona
    }
    return render(request, 'create_persona.html', context=context)


def list_personas(request):
    personas = Persona.objects.all()
    context = {
        'personas' : personas
    }
    return render(request, 'familiares.html', context=context)