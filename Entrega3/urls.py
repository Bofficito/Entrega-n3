from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.inicio),
    path('lista', views.lista_eventos),
    path('evento/', views.detalle_evento),
    path('registrar/', views.registrar_usuario),
    path('buscar/', views.buscar_eventos),
    path('añadir/', views.añadir_eventos),
    path('asistencia/', views.registrar_asistencia),
]
