from django.shortcuts import render
from django.http import HttpResponse
from .models import Persona
# Create your views here.
def personaTestView(request):
    obj = Persona.objects.get(id=1)
    context ={
        'nombre': obj.nombre,
        'edad': obj.edad,
    }
    return render(request, 'personas/test.html', context)