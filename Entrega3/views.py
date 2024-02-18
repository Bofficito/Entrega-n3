from django.shortcuts import render, redirect
from .models import Evento
from .forms import EventoForm, UsuarioForm, BusquedaForm

def inicio(request):
    return render(request, "inicio.html")

def lista_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos_lista.html', {'eventos': eventos})

def detalle_evento(request):
    eventos = Evento.objects.all()
    return render(request, 'evento_detalle.html', {'eventos': eventos})

def añadir_eventos(request):
    if request.method == 'POST':
        añadir_form = EventoForm(request.POST)
        if añadir_form.is_valid():
            añadir_form.save()
            return redirect('evento_registrado_exitosamente')
    else:
        añadir_form = EventoForm()
    return render(request, 'registrar_eventos.html', {'form': añadir_form})

def registrar_usuario(request):
    if request.method == "POST":
        usuario_form = UsuarioForm(request.POST)
        if usuario_form.is_valid():
            usuario_form = usuario_form.save()
            return render(request, 'registrar_eventos.html')
    else:
        usuario_form = UsuarioForm()
    return render(request, "registrar_usuario.html", {"usuario_form": usuario_form})

def buscar_eventos(request):
    if request.method == 'POST':
        busca_form = BusquedaForm(request.POST)
        if busca_form.is_valid():
            busqueda = busca_form.cleaned_data['busqueda']
            eventos = Evento.objects.filter(nombre__icontains=busqueda)
            return render(request, 'eventos_lista.html', {'eventos': eventos, 'busqueda': busqueda})
    else:
        busca_form = BusquedaForm()
    return render(request, 'buscar_eventos.html', {'form': busca_form})

def registrar_asistencia(request, evento_id):
    if request.method == 'POST':
        asistencia_form = UsuarioForm(request.POST)
        if asistencia_form.is_valid():
            usuario = asistencia_form.save()
            evento = Evento.objects.get(pk=evento_id)
            asistencia = asistencia(usuario=usuario, evento=evento)
            asistencia.save()
            return render(request, 'eventos_lista.html')