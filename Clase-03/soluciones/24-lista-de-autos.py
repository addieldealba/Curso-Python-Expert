#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Modifica el script listas-de-productos.py para que imprima la lista de
de 3 autos, haciendo uso de la clase Auto(Producto) que además cuanta
con los atributos marca y modelo.
"""

# Se defina la clase Producto() con atributos: nombre, apellido paterno y
# edad.
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


# Se defina la clase Auto() con atributos: marca, modelo
class Auto(Producto):
    """ Se define el objeto Auto """
    def __init__(self, nombre, cantidad, precio, marca, modelo):
        """ Se define el constructor de la clase """

        # Se ejecuta el constructor de la clase padre
        super().__init__(nombre, cantidad, precio)

        # Se inicializan los atributos de la clase hija
        self.marca = marca
        self.modelo = modelo


def obtener_autos():
    """ Crea y regresa una lista de objetos de tipo Auto() """

    # Se crea la lista de objetos Auto()
    autos = [
        Auto("Vocho", 1, 10000.0, "VW", 2000),
        Auto("Cordoba", 1, 185000.0, "Seat", 2010),
        Auto("Camaro", 1, 299000.0, "Chevrolet", 2018)
    ]

    return autos

def imprimir_autos(lista, total):
    """
    Imprime la lista de productos en lista donde cada elemento debe ser
    de tipo Auto()
    """
    an = 15  # Ancho de columna nombre
    ac = 8   # Ancho de columna cantidad
    ap = 10  # Ancho de columna precio
    ast = 10 # Ancho de columna subtotal
    ama = 10 # Ancho de columna marca
    amo = 6  # Ancho de columna de modelo
    at = ama + an + amo + ap + 3  # Ancho total

    # Se imprime encabezado
    print("{:{}} {:{}} {:{}} {:{}}".format("Marca", ama, "Nombre", an,
        "Modelo", amo, "Precio", ap))
    # Imprime separador
    print("-" * at)
    # Imprime cada registro de productos
    for auto in lista:
        print("{:{}} {:{}} {:{}} {:{}.2f}".format(auto.marca, ama,
            auto.nombre, an, auto.modelo, amo, auto.precio, ap))
    # Imprime otro separador
    print("-" * at)
    print("{:{}} {:{}} {:>{}} {:{}.2f}".format("", ama,
        "", an, "Total", amo,
        total, ast))

### INICIAR AQUÍ ###
# Se hace uso de una función cuya única tarea es obtener y regresar la
# lista de objetos de tipo Producto.
lista_autos = obtener_autos()

# Se calcula el total usando listas de compresión
total = sum([a.subtotal for a in lista_autos])

# Se hace uso de una función cuya única tarea es imprimir la lista de
# autos
imprimir_autos(lista_autos, total)

