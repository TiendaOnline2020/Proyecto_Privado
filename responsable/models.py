from django.contrib import messages
from django.db import models
from django.contrib.auth.models import User, Group


from ubicacion.models import Region, Provincia, Distrito

# Create your models here.
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from Afiliados.generar_regiones import generar_regiones

regiones_eleccion = generar_regiones()
def validar_nombre_usuario(value):
    for letra in value:
        if letra == " ":
            raise ValidationError(
                _('%(value)s no puede ver un espacio'),
                params={'value': value},
            )

class Responsable(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    numero_telefono = models.CharField(max_length=12)
    numero_dni = models.CharField(max_length=8)
    region = models.CharField(max_length=25, choices=regiones_eleccion)
    staff = models.BooleanField(verbose_name="Seleccione si el Usuario es staff")
    grupo_staf = models.CharField(max_length=255, blank=True, null=True, verbose_name="Nombre de Grupo(opcional)")
    objeto_guardado = models.BooleanField(default=False)
    correo = models.EmailField(null=True, blank=True)
    def save(self, *args, **kwargs):
        self.staff = self.usuario.is_staff
        if not self.objeto_guardado:
            try:
                self.objeto_guardado = True
                usuario_responsable = User.objects.get(username=self.usuario.username)
                grupo_afiliado = Group.objects.get(name=self.grupo_staf)
                usuario_responsable.groups.add(grupo_afiliado)
                usuario_responsable.save()
            except:
                pass
        super(Responsable, self).save(*args, **kwargs)

    def __str__(self):
        return self.usuario.username



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