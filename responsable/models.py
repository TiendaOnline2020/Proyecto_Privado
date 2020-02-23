from django.db import models
from django.contrib.auth.models import User, Group
from smart_selects.db_fields import ChainedForeignKey

from ubicacion.models import Region, Provincia, Distrito

# Create your models here.

class Responsable(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    numero_telefono = models.CharField(max_length=12, null=True, blank=True)
    numero_dni = models.CharField(max_length=8, null=True, blank=True)
    region = models.CharField(max_length=25, null=True, blank=True)
    def save(self, *args, **kwargs):
        usuario_responsable = User.objects.get(username=self.usuario.username)
        usuario_responsable.is_staff = True
        try:
            grupo_afiliado = Group.objects.get(name='Grupo_Afiliado')
            usuario_responsable.groups.add(grupo_afiliado)
            usuario_responsable.save()
        except:
            pass
        super(Responsable, self).save(*args, **kwargs)

    def __str__(self):
        return self.usuario.username