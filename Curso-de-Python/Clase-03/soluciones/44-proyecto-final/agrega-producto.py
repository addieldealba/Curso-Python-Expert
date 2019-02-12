#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Agrega un producto al archivo productos.csv proporcionado por el usuario
"""

from notas.entrada import lee_entero, lee_decimal
from notas.producto import Producto

import csv

# Variables o constantes globales
NA_PRODUCTOS = "productos.csv"  # Nombre del archivo de productos

def lee_producto():
    """
    Lee un producto desde la entrada estándar y regresa un objeto
    de tipo Producto
    """
    nombre = input("Nombre del producto: ")
    cantidad = lee_entero("Cantidad [1]:", 1)
    precio = lee_decimal("Precio:")

    return Producto(nombre, cantidad, precio)


def guarda_producto(producto, nomarch):
    """ Agrega el producto al archivo nomarch en formato CSV """
    with open(nomarch, "a") as fcsv:
        csv_writer = csv.writer(fcsv)
        csv_writer.writerow(producto.row)
    print("El producto {} ha sido guardado en {}!".format(
        producto.nombre, nomarch))


def main():
    """ Función principal del script """
    producto = lee_producto()
    guarda_producto(producto, NA_PRODUCTOS)


### INICIAR AQUÍ ###
# Se hace que el script se pueda usar como módulo
if __name__ == "__main__":
    main()
