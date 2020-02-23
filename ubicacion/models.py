from django.db import models

# Create your models here.
class Region(models.Model):
    Nombre = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.Nombre.lower().capitalize()
    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regiones"

class Provincia(models.Model):
    Nombre = models.CharField(max_length=255, blank=True)
    region_id = models.IntegerField(null=True, blank=True)
    region_provincia = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.Nombre.lower().capitalize()

    class Meta:
        verbose_name = "Provincia"
        verbose_name_plural = "Provincias"

class Distrito(models.Model):
    Nombre = models.CharField(max_length=255, null=True, blank=True)
    provincia_id = models.IntegerField(null=True, blank=True)
    provincia_distrito = models.ForeignKey(Provincia, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.Nombre.lower().capitalize()
    class Meta:
        verbose_name = "Distrito"
        verbose_name_plural = "Distritos"