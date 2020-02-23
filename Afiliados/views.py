from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Afiliado
from .descarga import editar_pdf
from ubicacion.models import Region, Provincia, Distrito
from six.moves.html_parser import HTMLParser
from django.conf import settings
Lista_regiones = settings.LISTA_REGIONES
Lista_provincia = settings.LISTA_PROVINCIAS
Lista_distrito = settings.LISTA_DISTRITOS

@login_required()
def descargar_pdf(request,dni):
    afiliado_dni = get_object_or_404(Afiliado, numero_dni=dni)
    return editar_pdf(afiliado_dni)

def home(request):
    if not Region.objects.all().exists():
        for valor_region in Lista_regiones:
            valor_region_lista = valor_region.split(',')
            objeto_region = Region()
            objeto_region.id = int(valor_region_lista[0])
            h = HTMLParser()
            objeto_region.Nombre = str(h.unescape(valor_region_lista[1].replace("'", ""))).lower().capitalize()
            objeto_region.save()
    if not Provincia.objects.all().exists():
        for valor_provincia in Lista_provincia:
            valor_provincia_lista = valor_provincia.split(',')
            objeto_provincia = Provincia()
            objeto_provincia.id = int(valor_provincia_lista[0])
            h = HTMLParser()
            objeto_provincia.region_id = valor_provincia_lista[2]
            objeto_provincia.Nombre = str(h.unescape(valor_provincia_lista[1].replace("'", ""))).lower().capitalize()
            objeto_provincia_region = Region.objects.get(id=int(valor_provincia_lista[2]))
            objeto_provincia.region_provincia = objeto_provincia_region
            objeto_provincia.save()
    if not Distrito.objects.all().exists():
        for valor_distrito in Lista_distrito:
            valor_distrito_lista = valor_distrito.split(',')
            objeto_distrito = Distrito()
            objeto_distrito.id = int(valor_distrito_lista[0])
            h = HTMLParser()
            objeto_distrito.Nombre = str(h.unescape(valor_distrito_lista[1].replace("'", ""))).lower().capitalize()
            objeto_distrito.provincia_id = int(valor_distrito_lista[2])
            objeto_distrito_provincia = Provincia.objects.get(id=int(valor_distrito_lista[2]))
            objeto_distrito.provincia_distrito = objeto_distrito_provincia
            objeto_distrito.save()
    return redirect('/admin/')
