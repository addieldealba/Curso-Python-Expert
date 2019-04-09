#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Modifica el script listas-de-productos.py para que imprima ademas de los
3 atributos (nombre, cantidad y precio), el atributo subtotal haciendo
uso del decorador @property.
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


def obtener_productos():
    """ Crea y regresa una lista de objetos de tipo Producto() """

    # Se crea la lista de objetos Producto()
    productos = [
        Producto("Caja chica", 5, 100.0),
        Producto("Caja mediana", 3, 185.0),
        Producto("Caja grande", 1, 299.0)
    ]

    return productos

def imprimir_productos(lista, total):
    """
    Imprime la lista de productos en lista donde cada elemento debe ser
    de tipo Producto()
    """
    an = 15  # Ancho de columna nombre
    ac = 8   # Ancho de columna cantidad
    ap = 10  # Ancho de columna precio
    ast = 10 # Ancho de columna subtotal
    at = an + ac + ap + ast + 3  # Ancho total

    # Se imprime encabezado
    print("{:{}} {:{}} {:{}} {:{}}".format("Nombre", an, "Cantidad", ac,
        "Precio", ap, "Subtotal", ast))
    # Imprime separador
    print("-" * at)
    # Imprime cada registro de productos
    for producto in lista:
        print("{:{}} {:{}} {:{}.2f} {:{}.2f}".format(producto.nombre, an,
            producto.cantidad, ac, producto.precio, ap,
            producto.subtotal, ast))
    # Imprime otro separador
    print("-" * at)
    print("{:{}} {:{}} {:>{}} {:{}.2f}".format("", an,
        "", ac, "Total", ap,
        total, ast))

### INICIAR AQUÍ ###
# Se hace uso de una función cuya única tarea es obtener y regresar la
# lista de objetos de tipo Producto.
lista_productos = obtener_productos()

# Se calcula el total usando listas de compresión
total = sum([p.subtotal for p in lista_productos])

# Se hace uso de una función cuya única tarea es imprimir la lista de
# productos
imprimir_productos(lista_productos, total)

