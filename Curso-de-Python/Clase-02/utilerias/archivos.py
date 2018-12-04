#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

MÓDULO: archivos

Contiene funciones que permiten realizar operaciones con el sistema de
archivos del sistema operativo.

"""

import os


# Imprime una línea horizontal de longitud l
linea = lambda l: print("-" * l)

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

