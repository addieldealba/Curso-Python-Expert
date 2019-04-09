#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Modifica el script listas-de-productos.py para que imprima la lista de
de 3 calzados, haciendo uso de la clase Calzado(Producto) que además cuenta
con los atributos talla y color.
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


# Se defina la clase Calzado() con atributos: talla y color
class Calzado(Producto):
    """ Se define el objeto Calzado """
    def __init__(self, nombre, cantidad, precio, talla, color):
        """ Se define el constructor de la clase """

        # Se ejecuta el constructor de la clase padre
        super().__init__(nombre, cantidad, precio)

        # Se inicializan los atributos de la clase hija
        self.talla = talla
        self.color = color


def obtener_calzados():
    """ Crea y regresa una lista de objetos de tipo Calzados() """

    # Se crea la lista de objetos Calzados()
    calzados = [
        Calzado("Steve Madden", 2, 1000.0, 5, "Blanco"),
        Calzado("Regina romero", 3, 1500.0, 6, "Perla"),
        Calzado("Scapino", 1, 2500.0, 8, "Café")
    ]

    return calzados

def imprimir_calzados(lista, total):
    """
    Imprime la lista de productos en lista donde cada elemento debe ser
    de tipo Calzado()
    """
    an = 15  # Ancho de columna nombre
    ac = 8   # Ancho de columna cantidad
    ap = 10  # Ancho de columna precio
    ast = 10 # Ancho de columna subtotal
    ata = 10 # Ancho de columna talla
    aco = 6  # Ancho de columna color
    at = an + aco + ac + ap + 3  # Ancho total

    # Se imprime encabezado
    print("{:{}} {:{}} {:{}} {:{}}".format("Nombre", an, "Color", aco,
        "Cantidad", ac, "Precio", ap))
    # Imprime separador
    print("-" * at)
    # Imprime cada registro de productos
    for calzado in lista:
        print("{:{}} {:{}} {:{}} {:{}.2f}".format(calzado.nombre, an,
            calzado.color, aco, calzado.cantidad, ac, calzado.precio, ap))
    # Imprime otro separador
    print("-" * at)
    print("{:{}} {:{}} {:>{}} {:{}.2f}".format("", an,
        "", aco, "Total", ac,
        total, ap))

### INICIAR AQUÍ ###
# Se hace uso de una función cuya única tarea es obtener y regresar la
# lista de objetos de tipo Calzado.
lista_calzados = obtener_calzados()

# Se calcula el total usando listas de compresión
total = sum([c.subtotal for c in lista_calzados])

# Se hace uso de una función cuya única tarea es imprimir la lista de
# calzados
imprimir_calzados(lista_calzados, total)

