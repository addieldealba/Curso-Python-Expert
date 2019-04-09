#!/usr/bin/env python
# -*- coding: utf-8 -*-


from notas.entrada import lee_producto
from notas.producto import Producto
from notas.salida import guarda_producto

import click
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
    producto = Producto(nombre, cantidad, precio)
    guarda_producto(producto, NA_PRODUCTOS)


### INICIAR AQUÍ ###
if __name__ == "__main__":
    agrega_producto()
