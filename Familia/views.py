from django.http import HttpResponse
from django.template import Template, Context, loader
from Familia.models import Familiar
from django.shortcuts import render
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