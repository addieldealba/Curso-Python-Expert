#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Crear e imprimir una lista de tres productos donde cada producto incluya
nombre, cantidad y precio, además cada producto deberá de ser una
instancia de la clase Producto(). Se debe hacer uso de las funciones
obtener_productos() e imprimir_productos().
"""

# Se defina la clase Persona() con atributos: nombre, apellido paterno y
# edad.
class Producto:
    """ Se define el objeto Producto """
    def __init__(self, nombre, cantidad, precio):
        """ Se define el constructor de la clase """

        # Se inicializan los atributos
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio


def obtener_productos():
    """ Crea y regresa una lista de objetos de tipo Producto() """

    # Se crea la lista de objetos Producto()
    productos = [
        Producto("Caja chica", 5, 100.0),
        Producto("Caja mediana", 3, 185.0),
        Producto("Caja grande", 1, 299.0)
    ]

    return productos

def imprimir_productos(lista):
    """
    Imprime la lista de productos en lista donde cada elemento debe ser
    de tipo Producto()
    """
    an = 15  # Ancho de columna nombre
    ac = 8   # Ancho de columna cantidad
    ap = 10  # Ancho de columna precio
    at = an + ac + ap + 2  # Ancho total

    # Se imprime encabezado
    print("{:{}} {:{}} {:{}}".format("Nombre", an, "Cantidad", ac,
        "Precio", ap))
    # Imprime separador
    print("-" * at)
    # Imprime cada registro de productos
    for producto in lista:
        print("{:{}} {:{}} {:{}.2f}".format(producto.nombre, an,
            producto.cantidad, ac, producto.precio, ap))
    # Imprime otro separador
    print("-" * at)

### INICIAR AQUÍ ###
# Se hace uso de una función cuya única tarea es obtener y regresar la
# lista de objetos de tipo Producto.
lista_productos = obtener_productos()

# Se hace uso de una función cuya única tarea es imprimir la lista de
# productos
imprimir_productos(lista_productos)

