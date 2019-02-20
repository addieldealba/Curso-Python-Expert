#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Define la clase Producto así como las funciones y constantes auxilares
para este objeto.
"""

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


