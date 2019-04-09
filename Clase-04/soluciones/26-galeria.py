#!/usr/bin/env python
# -*- coding: utf-8 -*-


from utilerias import archivos

import click
import os
import sys

@click.command()
@click.option("--html", is_flag=True,
    help="Imprime la lista en formato html")
@click.option("--out", "archivo", metavar="ARCHIVO",
    help="Guarda la lista en ARCHIVO en lugar de la salida estándar")
@click.argument("directorio", default=".", type=click.Path(exists=True))
def galeria(html, archivo, directorio):
    """
    Imprime en la salida estándar la lista de archivos jpg o png del
    DIRECTORIO proporcionado, si DIRECTORIO no se indica se imprimen los
    archivos del directorio actual. Si el directorio indicado no existe
    se muestra un mensaje de error.
    """
    lista_archivos = archivos.obtiene_archivos(directorio)

    # Sólo queremos los archivos con extensión .jpg o .png
    lista_archivos = [a for a in lista_archivos
            if a.ext().lower() in [".jpg", ".png"]]
    if html:
        doc_html = archivos.crea_galeria_html(lista_archivos, directorio)
        if archivo:
            archivos.guardar(doc_html, archivo)
        else:
            print(doc_html)
    else:
        if archivo:
            archivos.guardar_archivos(lista_archivos, archivo=archivo)
        else:
            archivos.imprime(lista_archivos)

### INICIAR AQUÍ ###
if __name__ == "__main__":
    galeria()


