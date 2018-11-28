#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

El script deberá imprimir la lista de productos actual y luego preguntar
si se desea agregar un producto, si sí, entonces leer el nombre y precio
del nuevo producto, si no entonces terminar. Cada que se agrega un
producto es necesario imprimir la lista de productos en orden
alfabético.

"""

# Se crea una lista de listas con todos la lista de productos iniciales
productos = [
    ("Automóvil", 150000.00),
    ("Bicicleta", 13000.00),
    ("Chamarra", 3999.99)
]

def imprimir(producto):
    """
    Imprime la tabla de productos en la salida estándar
    """
    # Se inicia la impresión de la tabla
    a_tabla = 65  # El ancho de la tabla
    a_producto = 50  # El ancho del campo producto
    a_precio = 10  # El ancho del campo precio

    print("-" * a_tabla)
    print("{:{}} | {:{}}".format("PRODUCTO", a_producto,
        "PRECIO", a_precio))
    print("-" * a_tabla)

    # Se hace uso de los ciclos for para imprimir los productos
    for producto in productos:
        print("{:{a_pro}} | {:{a_pre}.2f}".format(*producto,
            a_pro=a_producto, a_pre=a_precio))

    print("-" * a_tabla)


def lee_producto():
    """
    Lee un producto desde la entrada estándar y pregunta al usuario si
    desea agregar más productos, si si se lee un producto y se regresa
    como valor de la función, si no, entonces se regresa None.
    """
    # Se pregunta si quiere adicionar más productos
    print()
    if input("Desea agregar otro producto? (s/n) ").lower() not in ["si", "s"]:
        # Terminamo aquí, el usuario ya no quiere nada más
        return None
    # Se lee el nuevo producto
    print()
    resp = input("Capturar nuevo producto (nombre, precio): ")
    if resp == "":
        # Si la respuesta es vacía, regresamos una tupla vacía
        return tuple()
    else:
        # Si hay un producto, entonces creamos un tupla con los datos
        resp = resp.split(",")
        return resp[0], float(resp[1])
    print()


def adiciona(producto, productos):
    """
    Adiciona producto a la lista de productos
    """
    # Adiciona el producto a la lista
    productos.append(producto)

    # Ordena los productos
    productos.sort()

# COMENZAR AQUI!!!
# Agregamos productos infinitamente hasta que el usuario decida terminar
while True:
    imprimir(productos)
    producto = lee_producto()
    if producto == None:
        # Si no hay más productos terminamos
        break  # Esta instrucción rompe el ciclo while y termina
    elif producto == tuple():
        # Si el producto está vacío no hacemos nada
        pass
    else:
        # Si llegamos aquí tenemos un producto
        adiciona(producto, productos)


