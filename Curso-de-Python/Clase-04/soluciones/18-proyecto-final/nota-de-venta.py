#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Crea una nota de venta mostrando la lista de los productos, incluyendo
encabezado de columnas e iva desglozado. La nota resultante se guarda en
el archivo nota.csv
"""

from notas.entrada import obtiene_productos_csv
from notas.salida import guarda_nota_csv

# Variables o constantes globales
NA_PRODUCTOS = "productos.csv"  # Nombre del archivo de productos
NA_NOTA = "nota.csv"  # Nombre del archivo de la nota

### INICIAR AQUÍ ###
def main():
    """
    Función principal encargada de realizar el flujo principal del
    programa.
    """

    # Se obtiene la lista de productos desde el archivo productos.csv,
    # cada elemento de la lista es de tipo Producto
    productos = obtiene_productos_csv(NA_PRODUCTOS)

    # Se calcula el total e iva
    subtotal = sum([p.subtotal for p in productos])
    iva = round(subtotal * 0.16, 2)

    # Se guarda la nota en el archivo nota.csv 
    guarda_nota_csv(productos, subtotal, iva, NA_NOTA)


# Hacemos que el script se pueda usar como módulo también
if __name__ == "__main__":
    main()

