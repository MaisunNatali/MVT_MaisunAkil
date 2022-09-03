from django.http import HttpResponse
from django.template import Template, Context, loader
from Familia.models import Familiar
from django.shortcuts import render
from Familia.forms import FamiliarFormulario
# Create your views here.

def listar_familia(request):
    queryset=Familiar.objects.all()
    diccionario={'familia':queryset}
    plantilla=loader.get_template('Familia/familia_list.html')
    documento_html=plantilla.render(diccionario)

    return HttpResponse(documento_html)

def inicio(request):
    return render(request,"Familia/inicio.html" )


def familiar(request, id):
    queryset=Familiar.objects.get(id=id)
    diccionario={'miembro':queryset}
    plantilla=loader.get_template('Familia/familiar.html')
    documento_html=plantilla.render(diccionario)

    return HttpResponse(documento_html)

def familia_formulario(request):
    if request.method =='POST':
        formulario=FamiliarFormulario(request.POST)

        if formulario.is_valid():
            data=formulario.cleaned_data
            familia=Familiar(nombre=data['nombre'],fecha_nacimiento=data['fecha_nacimiento'],altura=data['altura'])
            familia.save()
            return render(request,'Familia/inicio.html')

    else:
        formulario=FamiliarFormulario()

    return render(request,'Familia/form_familia.html',{"formulario":formulario})
