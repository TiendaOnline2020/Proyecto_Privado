from django.contrib import admin
from .models import Responsable
# Register your models here.

class Responsable_Admin(admin.ModelAdmin):
    fields = (
        'usuario',
        'numero_telefono',
        'numero_dni',
        'region',
    )
    list_display = (
        'nombre_usuario',
        'numero_telefono',
        'numero_dni',
        'region'
    )
    def nombre_usuario(self, obj):
        return obj.usuario.username

admin.site.register(Responsable, Responsable_Admin)