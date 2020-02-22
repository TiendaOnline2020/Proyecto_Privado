from django.conf import settings
from django.http import FileResponse
from django.shortcuts import render
from io import BytesIO
# Create your views here.
from.models import Afiliado
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from PyPDF2 import PdfFileWriter, PdfFileReader


def editar_pdf(afiliado=Afiliado()):

    #Se nombran los Archivos.
    nombre_pdf_original = settings.ARCHIVO_PDF_ORIGINAL  #Documento original
    nombre_pdf_salida = settings.ARCHIVO_PDF_GUARDADO.format(afiliado.numero_dni)  # Nombre de pdf guardada

    #Se crea un pdf con ubicaciones.
    packet = BytesIO()
    c = canvas.Canvas(packet, pagesize=A4)
    c.setLineWidth(.3)
    if afiliado.organizacion_polita == 'N':
        c.drawString(224, 596, 'X')
    else:
        print("eeee")
        c.drawString(295, 596, 'X')
        c.drawString(347, 600, afiliado.organizacion_politica_region)


    c.drawString(167.3, 566, str(afiliado.fecha_afiliacion.strftime('%d'))) #dia afiliacion
    c.drawString(190, 566, str(afiliado.fecha_afiliacion.strftime('%m'))) #mes afiliacion
    c.drawString(218, 566, str(afiliado.fecha_afiliacion.strftime('%Y')))#año afiliacion
    c.drawString(35, 475, afiliado.apellido_paterno_afiliado) #apellido Paterno
    c.drawString(205, 475, afiliado.apellido_materno_afiliado ) #apellido Materno
    c.drawString(374, 475, afiliado.nombre_afiliado) #Nombre completo
    c.drawString(35, 422, afiliado.numero_dni) #numero de dni
    lista_nacimiento = afiliado.fecha_nacimiento_afiliado.split('/')
    c.drawString(235, 425, lista_nacimiento[0]) #dia nacimiento
    c.drawString(259, 425, lista_nacimiento[1]) #mes nacimiento
    c.drawString(282, 425, lista_nacimiento[2]) #anio nacimiento
    c.drawString(35, 382.5, afiliado.lugar_nacimiento) #lugar nacimiento
    '''Ubicacion Actual'''
    c.drawString(35, 323, afiliado.region_afiliado_guardado) #Departamento
    c.drawString(220, 325, afiliado.provincia_afiliado_guardado) #Provincia
    c.drawString(400, 325, afiliado.distrito_afiliado_guardado) #distrito

    c.drawString(35, 283, afiliado.avenida_afiliado)
    c.drawString(489, 283, afiliado.avenida_numero_afiliado)
    c.drawString(35, 245, afiliado.urbanizacion_afiliado)
    c.drawString(489, 245, afiliado.urbanizacion_numero_afiliado)
    c.drawString(35, 205, afiliado.correo)
    c.line(257, 90, 395, 90)
    c.drawString(470, 717, str(afiliado.id))

    '''
    '''
    estado_civil_opciones = (
        ('S', 'Civil'),
        ('C', 'Casado'),
        ('V', 'Viudo/a'),
        ('D', 'Divorciodo/a'),
        ('Conv', 'Conviviente')
    )

    c.setFont('Helvetica', 30)
    if afiliado.estado_civil == 'S':
        c.drawString(328, 418.7, 'X')  # Soltero
    elif afiliado.estado_civil == 'C':
        c.drawString(348.9, 418.7, 'X')  # Casado
    elif afiliado.estado_civil == 'V':
        c.drawString(370, 418.7, 'X')  # Viudo
    elif afiliado.estado_civil == 'D':
        c.drawString(391.8, 418.7, 'X')  # Divorciado
    elif afiliado.estado_civil == 'C':
        c.drawString(415.5, 418.7, 'X')  # Conviviente
    '''
    '''
    if afiliado.sexo == 'Femenino':
        c.drawString(474.3, 418.7, 'X')  # Femenino
    else:
        c.drawString(453, 418.7, 'X')  # Masculino
    '''
    '''
    c.save()

    packet.seek(0)

    pdf_con_pie = PdfFileReader(packet)

    pdf_existente = PdfFileReader(open(nombre_pdf_original, "rb"))

    output = PdfFileWriter()

    # Iterar desde 0 hasta el número de páginas de nuestro documento
    numero_de_paginas = pdf_existente.getNumPages()
    for numero in range(0, numero_de_paginas):
        page = pdf_existente.getPage(numero)
        page.mergePage(pdf_con_pie.getPage(0))
        output.addPage(page)

    outputStream = open(nombre_pdf_salida, "wb")

    output.write(outputStream)

    packet.close()
    response = FileResponse(open(nombre_pdf_salida, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment;filename=Afiliado-{}.pdf'.format(afiliado.numero_dni)

    return response