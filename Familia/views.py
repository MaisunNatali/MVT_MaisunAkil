from django.http import HttpResponse
from django.template import Template, Context, loader
from Familia.models import Familiar
# Create your views here.

def listar_familia(request):
    queryset=Familiar.objects.all()
    diccionario={'familia':queryset}
    plantilla=loader.get_template('familia_list.html')
    documento_html=plantilla.render(diccionario)

    return HttpResponse(documento_html)