from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import Responsable_Form
from .models import Responsable
# Create your views here.
def Registar_Responsable(request):
    form = Responsable_Form()
    contexto = {
        'form': form,
    }
    if request.method == 'POST':
        formulario = Responsable_Form(request.POST)
        if formulario.is_valid():
            contra1 = formulario.cleaned_data.get('contra1')
            contra2 = formulario.cleaned_data.get('contra2')
            if not len(contra1) >= 6:
                messages.info(request, "Minimo 6 digitos")
                return redirect('responsable:registro')
            if not contra1 == contra2 :
                messages.info(request,'Cotraseñas diferentes')
                return redirect('responsable:registro')
            usuario = User.objects.create_user(formulario.cleaned_data.get('Nombre_Usuario'),formulario.cleaned_data.get('Email'),formulario.cleaned_data.get('contra1'))
            usuario.first_name = formulario.cleaned_data.get('Nombre_Responsable')
            usuario.last_name = formulario.cleaned_data.get('Apellido_Paterno_Responsable') + formulario.cleaned_data.get('Apellido_Materno_Responsable')
            usuario.save()
            responsable_usuario = Responsable()
            responsable_usuario.usuario = usuario
            responsable_usuario.numero_dni = formulario.cleaned_data.get('Numero_Dni')
            responsable_usuario.numero_telefono = formulario.cleaned_data.get('Telefono')
            responsable_usuario.region = formulario.cleaned_data.get('Region')
            responsable_usuario.save()
            return redirect('afiliados:casa')

    return render(request, "registro_responsable.html", contexto)