from django.contrib import admin
from .models import Region, Provincia, Distrito
from six.moves.html_parser import HTMLParser


# Register your models here.

class Ubicacion_Region(admin.ModelAdmin):
    list_display = (
        'Nombre',
    )
    actions = ('Actualizar_Nombres',)

    def get_ordering(self, request):
        return ('Nombre',)

    def Actualizar_Nombres(self, request, queryset):
        for region in queryset:
            h = HTMLParser()
            region.Nombre = str(h.unescape(region.Nombre)).lower().capitalize()
            region.save()


class Ubicacion_Provincia(admin.ModelAdmin):
    list_display = (
        'Nombre',
    )
    actions = (
        'Actualizar_Nombres',
        'Actualizar_Regiones',
    )

    def get_ordering(self, request):
        return ('Nombre',)

    def Actualizar_Nombres(self, request, queryset):
        for provincia in queryset:
            h = HTMLParser()
            provincia.Nombre = str(h.unescape(provincia.Nombre)).lower().capitalize()
            provincia.save()

    def Actualizar_Regiones(self, request, queryset):
        for provincia in queryset:
            region = Region.objects.get(id=provincia.region_id)
            provincia.region_provincia = region
            provincia.save()


class Ubicacion_Distrito(admin.ModelAdmin):
    list_display = ('Nombre',)
    actions = ('Actualizar_Nombres', 'Actualizar_Distrito',)

    def get_ordering(self, request):
        return ('Nombre',)

    def Actualizar_Nombres(self, request, queryset):
        for distrito in queryset:
            h = HTMLParser()
            distrito.Nombre = str(h.unescape(distrito.Nombre)).lower().capitalize()
            distrito.save()

    def Actualizar_Distrito(self, request, queryset):
        for distrito in queryset:
            provincia = Region.objects.get(id=distrito.provincia_id)
            distrito.provincia_distrito = provincia
            distrito.save()


admin.site.register(Region, Ubicacion_Region)
admin.site.register(Provincia, Ubicacion_Provincia)
admin.site.register(Distrito, Ubicacion_Distrito)

