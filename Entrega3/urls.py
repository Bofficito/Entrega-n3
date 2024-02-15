from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.inicio),
    path('lista', views.lista_eventos),
    path('evento/', views.detalle_evento),
    path('registrar/', views.registrar_asistencia),
    path('buscar/', views.buscar_eventos),
]
