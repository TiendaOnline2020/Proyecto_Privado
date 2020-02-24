from django.contrib import admin
from .models import Responsable
from django import forms
# Register your models here.

class Responsable_Admin(admin.ModelAdmin):
    fields = (
        'usuario',
        'numero_telefono',
        'correo',
        'numero_dni',
        'region',
        'staff',
        'grupo_staf'
    )
    list_display = (
        'nombre_usuario',
        'numero_telefono',
        'numero_dni',
        'region',
        'staff',
    )
    def nombre_usuario(self, obj):
        return obj.usuario.username
    nombre_usuario.allow_tags = True
    nombre_usuario.short_description = 'Nombre Usuario'
    actions = ['crear_staff','eliminar_staff','eliminar_responsable']

    def crear_staff(self, request, queryset):
        for usuario in queryset:
            usuario.usuario.is_staff = True
            usuario.staff = True
            usuario.usuario.save()
            usuario.save()
    crear_staff.short_description = "Dar permisos staff"
    def eliminar_staff(self, request, queryset):
        for usuario in queryset:
            usuario.usuario.is_staff = False
            usuario.staff = False
            usuario.usuario.save()
            usuario.save()
    def eliminar_responsable(self, request, queryset):
        for usuario in queryset:
            usuario.usuario.delete()
            usuario.delete()

    eliminar_staff.short_description = "Quitar permisos staff"
    eliminar_responsable.shor_description = 'Eliminar Resposanble'

admin.site.register(Responsable, Responsable_Admin)