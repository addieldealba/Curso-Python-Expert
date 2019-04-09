#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

MÓDULO: archivos

Contiene funciones que permiten realizar operaciones con el sistema de
archivos del sistema operativo.

"""

import csv
import datetime
import os


class Archivo:
    """ Se define la clase para el objeto Archivo """
    def __init__(self, nombre, tamanio, fecha):
        """
        Contructor de la clase con los atributos nombre del archivo,
        tamanio en bytes y fecha en timestamp o en datetime.
        """
        self.nombre = nombre
        self.tamanio = tamanio
        if type(fecha) == float or type(fecha) == int:
            self.fecha = datetime.datetime.fromtimestamp(fecha)
        else:
            self.fecha = fecha

    @property
    def row(self):
        """
        Regresa una lista de los atributos a incluir en una línea de
        un archivo csv
        """
        return [self.nombre, self.tamanio,
            self.fecha.strftime("%b %d %Y %H:%M")]

# Imprime una línea horizontal de longitud l
linea = lambda l: print("-" * l)

def obtiene_archivos():
    """
    Obtiene la lista de archivos del directorio actual y regresa la lista
    ordenada en base al tamaño en bytes del mayor al menor.
    """
    # Se obtiene la lista de archivos usando el módulo os
    archivos = os.listdir()

    # Se obtiene el tamaño en bytes y la fecha de modificación usando
    # el módulo os.path y se crea un objeto Archivo
    archivos = [
        Archivo(a, os.path.getsize(a), os.path.getmtime(a))
        for a in archivos
    ]

    # Se ordena la lista en base al tamaño
    archivos.sort(key=lambda a: a.tamanio, reverse=True)

    return archivos

# Imprime la lista de archivo en forma de tabla
imprime = lambda archivos: print("\n".join(["{:40} {:10}".format(*a.row)
    for a in archivos]))

def guardar_archivos(lista, agregar=False):
    """
    Guarda la lista en archivos.csv donde cada elemento debe contar
    una representación en str.
    """
    # Se define el ancho máximo de cada línea en el archivo
    maxcols = 80
    if agregar:
        modo = "a"
    else:
        modo = "w"

    with open("archivos.csv", modo) as fcsv:
        # Se crea un escritor de tipo csv
        csv_writer = csv.writer(fcsv)
        # Guarda cada archivo
        for archivo in lista:
            csv_writer.writerow(archivo.row)


def main():
    """ Función principal que se ejecuta cuando es usado como script """

    archivos = obtiene_archivos()
    linea(51)
    imprime(archivos)
    linea(51)


# Las siguiente línea se ejecutan sólo cuando la variable interna de
# Python __name__ es igual a __main__, lo que significa que el script es
# el programa principal y por lo tanto se puede ejecutar la función
# main().
if __name__ == "__main__":
    main()

