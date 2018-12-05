from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from web.models import Empleado


class RegistroForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo electrónico',
        }


class EmpleadoForm(forms.ModelForm):

    class Meta:
        model = Empleado
        fields = [
            'nombre',
            'apellido',
            'tipo_de_documento',
            'numero_de_documento',
        ]
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'tipo_de_documento': 'Tipo de Documento',
            'numero_de_documento': 'Numero de Documento',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_de_documento': forms.Select(attrs={'class': 'form-control'}),
            'numero_de_documento': forms.TextInput(
                attrs={'class': 'form-control'}),
        }
