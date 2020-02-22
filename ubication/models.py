from django.db import models

# Create your models here.
class Region(models.Model):
    Nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.Nombre.lower().capitalize()


class Provincia(models.Model):
    Nombre = models.CharField(max_length=255)
    region_id = models.IntegerField()
    region_provincia = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=True)
    informacion_actualizada = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.Nombre.lower().capitalize()


class Distrito(models.Model):
    Nombre = models.CharField(max_length=255)
    provincia_id = models.IntegerField()
    provincia_distrito = models.ForeignKey(Provincia, on_delete=models.CASCADE, null=True, blank=True)
    informacion_actualizada = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.Nombre.lower().capitalize()
