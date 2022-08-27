from django.urls import path
from Familia.views import listar_familia

urlpatterns = [
    path('', listar_familia),
]
