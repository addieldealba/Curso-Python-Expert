#!/usr/bin/env python
# -*- coding: utf-8 -*-


from notas.entrada import obtiene_productos_csv
from notas.salida import (imprime, imprime_html, guarda, guarda_html,
        imprime_json, guarda_json)

import click

# Variables o constantes globales
NA_PRODUCTOS = "productos.csv"  # Nombre del archivo de productos

@click.command()
@click.option("--html", is_flag=True,
        help="Imprime la lista en formato HTML")
@click.option("--json", "es_json", is_flag=True,
        help="Imprime la lista en formato JSON")
@click.option("--out", "archivo", metavar="ARCHIVO",
        help="Guarda la lista en ARCHIVO en lugar de la salida estándar")
def lp(html, es_json, archivo):
    """
    Imprime en la salida estándar la lista de productos en formato de texto
    """

    # Se obtiene la lista de productos desde el archivo productos.csv,
    # cada elemento de la lista es de tipo Producto
    productos = obtiene_productos_csv(NA_PRODUCTOS)

    # Se inicia la lógica dada por las opciones
    if html:
        if archivo:
            # Se guarda en formato html
            guarda_html(archivo, productos)
        else:
            # Se imprime en formato html
            imprime_html(productos)
    elif es_json:
        if archivo:
            # Se guarda en formato json
            guarda_json(archivo, productos)
        else:
            # Se imprime en formato json
            imprime_json(productos)
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

