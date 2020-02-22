from django.db import models
from ubication.models import Region,Provincia,Distrito
# Create your models here.

class Todos_False(models.Model):
    nombre = models.CharField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        provincias = Provincia.objects.all()
        for provincia in provincias:
            provincia.informacion_actualizada = False
            provincia.save()
        distritos = Distrito.objects.all()
        for distrito in distritos:
            distrito.informacion_actualizada = False
            distrito.save()
        super(Todos_False, self).save(*args, **kwargs)

    def __str__(self):
        return "Informacion"+str(self.id)

class Actualizar(models.Model):
    nombre = models.CharField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        provincias = Provincia.objects.filter(informacion_actualizada=False)
        for provincia in provincias:
            objeto_region = Region.objects.get(id=provincia.region_id)
            provincia.region_provincia = objeto_region
            provincia.informacion_actualizada = True
            provincia.save()

        distritos = Distrito.objects.filter(informacion_actualizada=False)
        for distrito in distritos:
            provincia_objeto = Provincia.objects.get(id=distrito.provincia_id)
            distrito.provincia_distrito = provincia_objeto
            distrito.informacion_actualizada = True
            distrito.save()

        super(Actualizar, self).save(*args, **kwargs)