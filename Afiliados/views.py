from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Afiliado
from .descarga import editar_pdf
@login_required()
def descargar_pdf(request,dni):
    afiliado_dni = get_object_or_404(Afiliado, numero_dni=dni)
    return editar_pdf(afiliado_dni)