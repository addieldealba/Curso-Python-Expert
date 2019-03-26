#!/usr/bin/env python
# -*- coding: utf-8 -*-


from notas.entrada import obtiene_productos_csv
from notas.salida import imprime, imprime_html, guarda, guarda_html

import click

# Variables o constantes globales
NA_PRODUCTOS = "productos.csv"  # Nombre del archivo de productos

@click.command()
@click.option("--html", is_flag=True,
        help="Imprime la lista en formato HTML")
@click.option("--out", "archivo", metavar="ARCHIVO",
        help="Guarda la lista en ARCHIVO en lugar de la salida estándar")
def lp(html, archivo):
    """
    Imprime en la salida estándar la lista de productos en formato de texto
    """

    # Se obtiene la lista de productos desde el archivo productos.csv,
    # cada elemento de la lista es de tipo Producto
    productos = obtiene_productos_csv(NA_PRODUCTOS)

    # Se inica la lógica dada por las opciones
    if html:
        if archivo:
            # Se guarda en formato html
            guarda_html(archivo, productos)
        else:
            # Se imprime en formato html
            imprime_html(productos)
    else:
        if archivo:
            # Se guarda en formato texto
            guarda(archivo, productos)
        else:
            # Se imprime en formato texto
            imprime(productos)

### INICIAR AQUÍ ###
if __name__ == "__main__":
    lp()

