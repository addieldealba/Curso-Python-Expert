#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Modifica el script listas-de-productos.py para que guarde 3 productos en
el archivo productos.csv con los atributos nombre, cantidad, precio y
subtotal. Se debe de hacer uso de la clase Producto. Al final se debe
agregar una línea más con el total.
"""

import csv

# Se define la clase Producto() con atributos: nombre, cantidad y precio
class Producto:
    """ Se define el objeto Producto """
    def __init__(self, nombre, cantidad, precio):
        """ Se define el constructor de la clase """

        # Se inicializan los atributos
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    @property
    def subtotal(self):
        """ Calcula el subtotal para cada producto """
        return self.cantidad * self.precio

    @property
    def row(self):
        """
        Regresa una lista con los elementos para ser guardados en un
        archivos CSV
        """
        return [self.nombre, self.cantidad, self.precio, self.subtotal]


def obtener_productos():
    """ Crea y regresa una lista de objetos de tipo Producto() """

    # Se crea la lista de objetos Producto()
    productos = [
        Producto("Caja chica", 5, 100.0),
        Producto("Caja mediana", 3, 185.0),
        Producto("Caja grande", 1, 299.0)
    ]

    return productos


def guarda_productos_csv(lista, total):
    """
    Guarda los productos en lista en el archivo productos.csv y en una
    fila adicional el total.
    """
    with open("productos.csv", "w") as fcsv:
        # Se crea una variable de tipo csv
        csv_writer = csv.writer(fcsv)

        # Se guarda cada uno de los productos en el archivo csv
        for producto in lista:
            csv_writer.writerow(producto.row)
        
        # Se construye la lista de la fila para el total
        fila_total = [None, None, None, total]
        csv_writer.writerow(fila_total)

    print("El archivo productos.csv ha sido creado!")
    print()


### INICIAR AQUÍ ###
# Se obtiene la lista de objetos de tipo Producto.
lista_productos = obtener_productos()

# Se calcula el total usando listas de compresión
total = sum([p.subtotal for p in lista_productos])

# Se guarda la lista de productos y el total
guarda_productos_csv(lista_productos, total)

