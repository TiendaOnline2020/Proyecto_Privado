from django.contrib import messages
from django.db import models
from django.contrib.auth.models import User, Group, AbstractUser

from ubicacion.models import Region, Provincia, Distrito

# Create your models here.
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from Afiliados.generar_regiones import generar_regiones
regiones_eleccion = generar_regiones()
class Responsable(AbstractUser):
    telefono = models.CharField(unique=True, null=True, blank=True,max_length=255)
    numero_dni = models.CharField(unique=True, null=True, blank=True, max_length=255)
    region = models.CharField(verbose_name="Region Encargada", choices=regiones_eleccion, max_length=255)

    def __str__(self):
        return self.username
'''

                if self.telefono:
            self.confirmacion_wsp = True
        if self.correo:
            self.confirmacion_correo = True
        if settings.MANDAR_MENSAJES_CORREO:
            subject = settings.ASUNTO
            message = settings.SALUDO.format(self.nombre_persona) + settings.MENSAJE
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [self.correo]
            email = EmailMessage(subject, message, email_from, recipient_list)
            email.send()
'''