#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Agrega un producto al archivo productos.csv proporcionado por el usuario
desde la línea de comandos.
"""

from notas.entrada import lee_producto
from notas.producto import Producto
from notas.salida import guarda_producto

import sys

# Variables o constantes globales
NA_PRODUCTOS = "productos.csv"  # Nombre del archivo de productos


def main(argv):
    """ Función principal del script """

    # Se valida que se proporcionen 3 parámetros
    if len(argv) == 3:
        # Tenemos un producto
        nombre = argv[0]
        # Se valida que el 2do argumento sea entero
        try:
            cantidad = int(argv[1])
        except ValueError:
            print("Error: la cantidad tiene que ser entero!")
            sys.exit(1)
        # Se valida que el 3er argumento sea decimal
        try:
            precio = float(argv[2])
        except ValueError:
            print("Error: el precio tiene que ser decimal")
            sys.exit(2)
    else:
        print("Error: sintaxis incorrecta!")
        print("""
Sintaxis:
    agrega-producto NOMBRE CANTIDAD PRECIO

        """)
        sys.exit(3)

    producto = Producto(nombre, cantidad, precio)
    guarda_producto(producto, NA_PRODUCTOS)


### INICIAR AQUÍ ###
# Se hace que el script se pueda usar como módulo
if __name__ == "__main__":
    main(sys.argv[1:])
