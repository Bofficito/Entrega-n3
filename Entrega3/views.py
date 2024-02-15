from django.shortcuts import render, redirect
from .models import Evento
from .forms import EventoForm, UsuarioForm, BusquedaForm

def inicio(request):
    return render(request, "index.html")

def lista_eventos(request):
    return render(request, "eventos_lista.html")

def detalle_evento(request):
    return render(request, "evento_detalle.html")

def registrar_asistencia(request):
    if request.method == "POST":
        usuario_form = UsuarioForm(request.POST)
        if usuario_form.is_valid():
            usuario = usuario_form.save()
            return render(request, "eventos_lista.html")
    else:
        usuario_form = UsuarioForm()
    return render(request, "registrar_asistencia.html", {"usuario_form": usuario_form})

def buscar_eventos(request):
    if request.method == "POST":
        form = BusquedaForm(request.POST)
        if form.is_valid():
            busqueda = form.cleaned_data["busqueda"]
            eventos = Evento.objects.filter(nombre__icontains=busqueda)
            return render(request, "resultados_busqueda.html", {"eventos": eventos, "busqueda": busqueda})
    else:
        form = BusquedaForm()
    return render(request, "buscar_eventos.html", {"form": form})
