from django.urls import path
from Familia.views import listar_familia,familiar,familia_formulario

urlpatterns = [
    path('', listar_familia, name="familia"),
    path('<int:id>/',familiar,name="familiares"),
    path('<int:id>/',familiar,name="familiares"),
    path('crear-familia/',familia_formulario, name="familia_formulario"),
]
