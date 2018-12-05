#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

MÓDULO entrada

Contiene todas las funciones que interactuan con el usuario o generan
una entrada de datos.

"""

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


def inicia_productos():
    """
    Se encarga de iniciar la lista de productos.

    Regresa una lista de tuplas, donde cada pruducto contiene los
    siguientes campos: (nombre, precio, cantidad)
    """

    # Los productos estarán en una lista de tuplas conteniendo
    # (nombre, precio, cantidad)
    # NOTA: Se elimina el valor de descuento para este caso
    productos = [
        ("Automóvil", 150000.00, 1),
        ("Bicicleta", 13000.00, 2),
        ("Chamarra", 3999.99, 2),
        ("Laptop Thinkpad", 25000.00, 1),
        ("Gafas de realidad virtual Lenovo con sable laser",
            5000.00, 2)
    ]

    return productos

