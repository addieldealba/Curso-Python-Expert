#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Sintaxis:
    lista-de-archivos.py DIRECTORIO 

Descripción:
Imprime la lista de archivos del DIRECTORIO proporcionado, si DIRECTORIO
no se indica se muestran los archivos del directorio actual. Si el
directorio indicado no existe se deberá mostrar un mensaje, pero evitar en
todo momento que el script termine en error lanzando alguna excepción.
"""

from utilerias import archivos

import os
import sys

def main(argv):
    """ función principal del script """
    if len(argv) == 1:
        directorio = argv[0]
        if not os.path.isdir(directorio):
            print("Error: el directorio {} no existe!".format(directorio))
            sys.exit(1)  # Se termina el script regresando al shell el error 1
    else:
        directorio = "."

    lista_archivos = archivos.obtiene_archivos(directorio)
    archivos.imprime(lista_archivos)

### INICIAR AQUÍ ###
if __name__ == "__main__":
    main(sys.argv[1:])


