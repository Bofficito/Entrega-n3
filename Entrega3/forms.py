from django import forms
from .models import Evento, Usuario

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nombre', 'descripcion', 'fecha', 'direccion', 'latitud', 'longitud']

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'correo']

class BusquedaForm(forms.Form):
    busqueda = forms.CharField(label='Buscar eventos')
