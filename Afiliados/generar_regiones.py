from django.conf import settings


def generar_regiones():
    regiones = settings.LISTA_REGIONES
    lista_regiones = []
    for i in regiones:
        lista_regiones.append(i.split(',')[1])
    lista_regiones_nueva = []
    for region_nombre in lista_regiones:
        region_nombre_nuevo = region_nombre.replace("'","").lower().capitalize()
        lista_moment = []
        lista_moment.append(region_nombre_nuevo)
        lista_moment.append(region_nombre_nuevo)
        tupla_moment = tuple(lista_moment)
        lista_regiones_nueva.append(tupla_moment)
    tupla_final = tuple(lista_regiones_nueva)
    return tupla_final