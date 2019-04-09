#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

MÓDULO entrada

Contiene todas las funciones que interactuan con el usuario o generan
una entrada de datos.

"""

from notas.producto import Producto

import csv

def leesino(msg):
    """
    Se lee la respuesta del usuario para elegir si quiere o no iva
    desglosado mostrando el mensaje msg. Si el usuario da una respuesta
    no válida se continua leyendo hasta obtener una respuesta válida.

    Regresa el valor de True si el usuario responde que si, regresa False
    si el usuario responde que no.
    """
    resp = None
    while resp == None:  # Mientras no tengamos respuesta correcta, seguimos
        print()  # Deja una línea en blanco
        valor = input(msg + " ")
        if valor.lower() == "s" or valor.lower() == "si":
            resp = True  # Si queremos iva desglosado
        elif valor.lower() in ["n", "no"]:  # versión compacta 
            resp = False  # No queremos iva desglosado
        else:
            print("    Error: {} no es una respuesta válida, intenta de nuevo.".
                format(valor))
    print()  # Deja una línea en blanco al final
    return resp


def lee_entero(msg, valor=None):
    """
    Lee un entero desde la entrada estándar mostrando el mensaje en msg y
    regresando el valor de tipo int.

    Si valor es diferente de None se regresa en caso de que el usuario no
    proporcione alguno.
    """

    # Hacemos un ciclo infinito hasta que se leea un entero
    while True:
        resp = input(msg + " ")
        # si la respuesta está vacía regresamos valor
        if resp == "" and valor != None:
            return valor
        # si no, entonces vemos si es un entero
        elif resp.isdigit():
            # Tenemos un entero y lo regresamos
            return int(resp)
        else:
            # Tenemos cualquier cosa, menos un entero
            print()
            print("Error: lo que has escrito no es un entero, intenta de nuevo!")
            print()


def lee_decimal(msg, valor=None):
    """
    Lee un decimal desde la entrada estándar mostrando el mensaje en msg y
    regresando el valor de tipo float.

    Si valor es diferente de None se regresa en caso de que el usuario no
    proporcione alguno.
    """

    # Hacemos un ciclo infinito hasta que se leea un decimal
    while True:
        resp = input(msg + " ")
        # si la respuesta está vacía regresamos valor
        if resp == "" and valor != None:
            return valor
        # si no, entonces vemos si es un decimal
        elif resp.replace(".", "").isdigit() :
            # Tenemos un entero o un decimal y lo regresamos
            return float(resp)
        else:
            # Tenemos cualquier otra cosa, menos un decimal
            print()
            print("Error: lo que has escrito no es un decimal, intenta de nuevo!")
            print()


def lee_producto():
    """
    Lee un producto desde la entrada estándar y regresa un objeto
    de tipo Producto
    """
    nombre = input("Nombre del producto: ")
    cantidad = lee_entero("Cantidad [1]:", 1)
    precio = lee_decimal("Precio:")

    return Producto(nombre, cantidad, precio)


def obtiene_productos_csv(nomarch):
    """
    Regresa la lista de productos donde cada elemento es de tipo Producto
    leídos desde el archivo nomarch
    """
    productos = []
    with open(nomarch) as fcsv:
        csv_reader = csv.reader(fcsv)
        for fila in csv_reader:
            producto = Producto(fila[0], int(fila[1]), float(fila[2]))
            productos.append(producto)

    return productos
