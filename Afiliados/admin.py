from django.contrib import admin
from django.utils.html import format_html

from .models import Afiliado
# Register your models here.


class Afiliado_Admin(admin.ModelAdmin):
    '''
    fields = (
        ('organizacion_polita','organizacion_politica_region',),
        'fecha_afiliacion',
        ('numero_dni','estado_civil'),
        'lugar_nacimiento',
        ('region_afiliado',
         'provincia_afiliado',
         'distrito_afiliado',),
        ('avenida_afiliado',
         'avenida_numero_afiliado',),
        ('urbanizacion_afiliado',
         'urbanizacion_numero_afiliado',),
        'correo',
    )
    '''
    fieldsets = [
        ('Organizacion Politica', {'fields': ['organizacion_polita', 'organizacion_politica_region']}),
        ('Fecha de Afiliación', {'fields': ['fecha_afiliacion']}),
        ('Datos Personales', {'fields': ['numero_dni', 'estado_civil', 'lugar_nacimiento']}),
        ('Domicilio Actual', {'fields': [
            ('region_afiliado',
            'provincia_afiliado',
            'distrito_afiliado',),
            ('avenida_afiliado',
            'avenida_numero_afiliado',),
            ('urbanizacion_afiliado',
            'urbanizacion_numero_afiliado',),
            'correo']}
        ),
    ]
    def my_url_field(self, obj):
        return format_html('<a href="%s%s">%s</a>' % ('http://127.0.0.1:8000/descargar/',obj.numero_dni,'Descargar Ficha Afiliación'))
    my_url_field.allow_tags = True
    my_url_field.short_description = 'Ficha Afiliación PDF'
    list_display = (
        'numero_dni',
        'nombre_afiliado',
        'apellido_paterno_afiliado',
        'apellido_materno_afiliado',
        'fecha_nacimiento_afiliado',
        'estado_civil',
        'sexo',
        'my_url_field',
    )
    search_fields = ('numero_dni','nombre_afiliado','apellido_paterno_afiliado','apellido_materno_afiliado')

admin.site.register(Afiliado, Afiliado_Admin)
