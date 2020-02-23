from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from .generar_regiones import generar_regiones
from django.conf import settings
from ubicacion.models import Region, Provincia, Distrito
import requests
# Create your models here.

estado_civil_opciones = (
    ('S', 'Civil'),
    ('C', 'Casado'),
    ('V', 'Viudo/a'),
    ('D', 'Divorciodo/a'),
    ('Conv', 'Conviviente')
)
organizacion_politica = (
    ('N', 'Nacional'),
    ('R', 'Regional')
)
regiones_eleccion = generar_regiones()

class Afiliado(models.Model):
    organizacion_polita = models.CharField(max_length=255, verbose_name="Alcance de la Organizacion Politica ",
                                           choices=organizacion_politica)
    organizacion_politica_region = models.CharField(max_length=255, null=True, choices=regiones_eleccion, blank=True, verbose_name="Region (opcional)")
    fecha_afiliacion = models.DateField(auto_now=False, auto_now_add=False)
    #Datos Personales
    numero_dni = models.CharField(max_length=8, verbose_name="Numero de DNI ")
    nombre_afiliado = models.CharField(max_length=250, verbose_name="Nombres")
    apellido_paterno_afiliado = models.CharField(max_length=250, verbose_name="Apellido Paterno")
    apellido_materno_afiliado = models.CharField(max_length=250, verbose_name="Apellido Materno")
    fecha_nacimiento_afiliado = models.CharField(max_length=255, verbose_name="Fecha Nacimiento")
    estado_civil = models.CharField(max_length=25, choices=estado_civil_opciones, verbose_name="Estado Civil ")
    sexo = models.CharField(max_length=20)
    lugar_nacimiento = models.CharField(max_length=255, verbose_name="Lugar de Nacimiento ")
    #Domicilio Actual

    region_afiliado = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=True)
    provincia_afiliado = ChainedForeignKey(
        Provincia,
        chained_field="region_afiliado",
        chained_model_field="region_provincia",
        show_all=False,
        auto_choose=True,
        sort=True,
    )
    distrito_afiliado = ChainedForeignKey(
        Distrito,
        chained_field="provincia_afiliado",
        chained_model_field="provincia_distrito",
        show_all=False,
        auto_choose=True,
        sort=True,
    )

    avenida_afiliado = models.CharField(max_length=255, verbose_name="Avenida/Calle/Jirón")
    avenida_numero_afiliado = models.CharField(max_length=25, verbose_name="Numero")
    urbanizacion_afiliado = models.CharField(max_length=255, verbose_name="Urbanizacion/Sector/Caserío")
    urbanizacion_numero_afiliado = models.CharField(max_length=25, verbose_name="Telefono")
    correo = models.EmailField(max_length=255)
    #domicilios guardados
    region_afiliado_guardado = models.CharField(null=True, blank=True, max_length=255)
    provincia_afiliado_guardado = models.CharField(null=True, blank=True, max_length=255)
    distrito_afiliado_guardado = models.CharField(null=True, blank=True, max_length=255)

    def save(self, *args, **kwargs):

        url = settings.URL_API

        contexto = {
            'strDni': str(self.numero_dni)
        }
        informacion = requests.get(url, contexto).json()['DatosPerson'][0]

        self.apellido_paterno_afiliado = str(informacion['ApellidoPaterno']).lower().capitalize()
        self.apellido_materno_afiliado = str(informacion['ApellidoMaterno']).lower().capitalize()

        nombres_separados = informacion['Nombres'].split()
        nombres = ""
        for i in nombres_separados:
            nombres += i.lower().capitalize()
            nombres += " "
        self.nombre_afiliado = nombres

        if informacion['Sexo'] == '2':
            self.sexo = "Masculino"
        elif informacion['Sexo'] == '3':
            self.sexo = "Femenino"


        self.fecha_nacimiento_afiliado = str(informacion['FechaNacimiento'])
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
        self.distrito_afiliado_guardado = self.distrito_afiliado.Nombre
        self.provincia_afiliado_guardado = self.provincia_afiliado.Nombre
        self.region_afiliado_guardado = self.region_afiliado.Nombre
        super(Afiliado, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre_afiliado

    class Meta:
        verbose_name_plural = "Afiliados"
        verbose_name = "Afiliado"

