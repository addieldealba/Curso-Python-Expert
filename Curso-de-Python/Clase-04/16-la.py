#!/usr/bin/env python
# -*- coding: utf-8 -*-


from utilerias import archivos

import click
import os
import sys

@click.command()
@click.argument("directorio", default=".", type=click.Path(exists=True))
def la(directorio):
    """
    Imprime en la salida estándar la lista de archivos del DIRECTORIO
    proporcionado, si DIRECTORIO no se indica se imprimen los archivos
    del directorio actual. Si el directorio indicado no existe se muestra
    un mensaje de error.
    """
    lista_archivos = archivos.obtiene_archivos(directorio)
    archivos.imprime(lista_archivos)

### INICIAR AQUÍ ###
if __name__ == "__main__":
    la()


