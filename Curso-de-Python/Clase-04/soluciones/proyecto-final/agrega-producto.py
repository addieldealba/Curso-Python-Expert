#!/usr/bin/env python
# -*- coding: utf-8 -*-


from producto import (Producto, obtiene_productos_csv, guarda_producto_csv,
        guarda_producto_imagen)

import click
import os
import sys

# Variables o constantes globales
NA_PRODUCTOS = "productos.csv"  # Nombre del archivo de productos
# Nombre de la carpeta donde se guardarán las imagenes de los productos
DIR_IMAGENES = "imagenes"

@click.command()
@click.argument("nombre")
@click.argument("cantidad", type=int)
@click.argument("precio", type=float)
@click.argument("rutaimagen", type=click.Path(exists=True), default="")
def agrega_producto(nombre, cantidad, precio, rutaimagen):
    """
    Agrega un producto proporcionado por el usuario desde la línea de
    comandos. Los atributos obligatorios son NOMBRE, CANTIDAD y PRECIO
    y el atributo RUTAIMAGEN es opcional. Si RUTAIMAGE está presente se
    hace una copia del archivo indicado a la carpeta DIR_IMAGENES con el
    nombre producto-id.ext
    """
    # Si ya hay un archivos de productos se lee para determinar el
    # siguiente id, de lo contrario el id sería el 1.
    if os.path.exists(NA_PRODUCTOS):
        lista = obtiene_productos_csv(NA_PRODUCTOS)
        id_producto = int(lista[-1].id) + 1
    else:
        id_producto = 1

    # Se procesa la rutaimagen
    if rutaimagen:
        imagen = "producto-{}{}".format(id_producto,
                os.path.splitext(rutaimagen)[1])
        guarda_producto_imagen(rutaimagen, DIR_IMAGENES, imagen)
    else:
        imagen = ""

    # Se agrega el producto
    producto = Producto(id_producto, nombre, cantidad, precio, imagen)
    guarda_producto_csv(producto, NA_PRODUCTOS)


### INICIAR AQUÍ ###
if __name__ == "__main__":
    agrega_producto()
