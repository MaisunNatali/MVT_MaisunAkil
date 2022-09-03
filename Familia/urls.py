from django.urls import path
from Familia.views import listar_familia,familiar

urlpatterns = [
    path('', listar_familia, name="familia"),
    path('<int:id>/',familiar,name="familiares"),
    
]
