#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

El script deberá de imprimir en la salida estándar la lista de archivos
del directorio actual ordenados en base al tamaño en bytes.

"""

import os


# Imprime una línea 
linea = lambda: print("-" * 51)

def obtiene_archivos():
    """
    Obtiene la lista de archivos del directorio actual y regresa la lista
    ordenada en base al tamaño en bytes.
    """
    # Se obtiene la lista de archivos usando el módulo os
    archivos = os.listdir()
    # Se obtiene el tamaño en bytes usando el módulo os.path
    archivos = [(a, os.path.getsize(a)) for a in archivos]
    # Se ordena la lista y para ordenarla en base al tamaño se le indica
    # a la función sort en su atributo key que use el segundo valor de
    # cada tupla como llave para el ordenamiento.
    archivos.sort(key=lambda t: t[1])

    return archivos

# Imprime la lista de archivo en forma de tabla
imprime = lambda archivos: print("\n".join(["{:40} {:10}".format(*a)
    for a in archivos]))


# INICIAR AQUÍ! Uso de funciones lambda
archivos = obtiene_archivos()
linea()
imprime(archivos)
linea()

