from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import forms
from django import forms
from .models import Responsable
from django.conf import settings
from Afiliados.generar_regiones import generar_regiones
choices_regiones = generar_regiones()

print(choices_regiones)
class Responsable_Form(forms.Form):
    Numero_Dni = forms.CharField(
        label='Numero de Dni', required=True, widget=forms.TextInput(attrs={'class': 'form-control input-sm','placeholder': 'Numero DNI'})
    )
    Nombre_Responsable = forms.CharField(
        label='Nombres', required=True, widget=forms.TextInput(attrs={'class': 'form-control input-sm','placeholder': 'Nombre Completo'})
    )
    Apellido_Paterno_Responsable = forms.CharField(
        label='Apellido Paterno', required=True, widget=forms.TextInput(attrs={'class': 'form-control input-sm'})
    )
    Apellido_Materno_Responsable = forms.CharField(
        label='Apellido Paterno', required=True, widget=forms.TextInput(attrs={'class': 'form-control input-sm'})
    )
    Nombre_Usuario = forms.CharField(
        label='Nombre Usuario', required=True, widget=forms.TextInput(attrs={'class': 'form-control input-sm'})
    )
    Email = forms.EmailField(
        label='Direccion Email', required=True, widget=forms.EmailInput(attrs={'class': 'form-control input-sm'})
    )
    Telefono = forms.CharField(
        label='Numero de telefono', required=True, widget=forms.TextInput(attrs={'class': 'form-control input-sm'})
    )
    Region = forms.ChoiceField(
        label='Region encargada', required=True, widget=forms.Select, choices=choices_regiones
    )
    contra1 = forms.CharField(
        label='Contraseña', required=True, widget=forms.PasswordInput(attrs={'class': 'form-control input-sm'})
    )
    contra2 = forms.CharField(
        label='Confirmar contraseña', required=True, widget=forms.PasswordInput(attrs={'class': 'form-control input-sm'})
    )
    clave = forms.CharField(
        label='Clave Unica', required=True, widget=forms.TextInput(attrs={'class': 'form-control input-sm'})
    )

