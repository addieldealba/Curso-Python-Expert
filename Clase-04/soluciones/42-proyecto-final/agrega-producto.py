#!/usr/bin/env python
# -*- coding: utf-8 -*-


from notas.entrada import lee_producto, obtiene_productos_csv
from notas.producto import Producto
from notas.salida import guarda_producto

import click
import os
import sys

# Variables o constantes globales
NA_PRODUCTOS = "productos.csv"  # Nombre del archivo de productos

@click.command()
@click.argument("nombre")
@click.argument("cantidad", type=int)
@click.argument("precio", type=float)
def agrega_producto(nombre, cantidad, precio):
    """
    Agrega un producto al archivo productos.csv proporcionado por el
    usuario desde la línea de comandos NOMBRE, CANTIDAD y PRECIO.
    """
    if os.path.exists(NA_PRODUCTOS):
        lista = obtiene_productos_csv(NA_PRODUCTOS)
    else:
        lista = []
    producto = Producto(len(lista) + 1, nombre, cantidad, precio)

    guarda_producto(producto, NA_PRODUCTOS)


### INICIAR AQUÍ ###
if __name__ == "__main__":
    agrega_producto()
