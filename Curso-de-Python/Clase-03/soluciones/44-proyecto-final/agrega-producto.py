#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Agrega un producto al archivo productos.csv proporcionado por el usuario
"""

from notas.entrada import lee_producto
from notas.salida import guarda_producto

# Variables o constantes globales
NA_PRODUCTOS = "productos.csv"  # Nombre del archivo de productos


def main():
    """ Función principal del script """
    producto = lee_producto()
    guarda_producto(producto, NA_PRODUCTOS)


### INICIAR AQUÍ ###
# Se hace que el script se pueda usar como módulo
if __name__ == "__main__":
    main()
