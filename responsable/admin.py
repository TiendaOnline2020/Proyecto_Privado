from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Responsable
from django import forms
# Register your models here.
from django.contrib.auth.admin import UserAdmin
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Responsable
        fields = ('telefono', 'region', 'numero_dni')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Responsable
        fields = ('email', 'telefono', 'region', 'numero_dni')
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Responsable
    list_display = ['username', 'email', 'telefono', 'region','is_staff']
    add_fieldsets =(
        ('Campos Usuario:',{
            'fields':('username',('password1', 'password2'),'is_staff',)
        }),
        ('Datos Personales:',{
            'fields':(('email','telefono'),('region', 'numero_dni'))
        }),
    )
    def eliminar_staff(self, request, queryset):
        for usuario in queryset:
            usuario.is_staff = False
            usuario.save()
    def agregar_staff(self, request, queryset):
        for usuario in queryset:
            usuario.is_staff = True
            usuario.save()
    actions = ['agregar_staff', 'eliminar_staff']
    eliminar_staff.short_description = "Quitar permisos staff"
    agregar_staff.short_description = "Agregar al Staff"


admin.site.register(Responsable, CustomUserAdmin)
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

