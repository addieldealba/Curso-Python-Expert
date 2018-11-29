#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

El script deberá:
1. Imprimir la lista de productos actual
2. Preguntar si se desea agregar un producto
3. SI, leer nombre y precio del nuevo producto
4. Agregar el nuevo producto a la lista de productos
5. Ordenar lista de productos
6. Regresar al paso 1.
7. NO, entonces terminamos

"""

# Se crea una lista de túplas que almacenará todos los productos
productos = [
    ("Automóvil", 150000.00),
    ("Bicicleta", 13000.00),
]

# Imprime una línea
imp_linea = lambda: print("-" * 65)

# Imprime un renglón de la tabla
imp_renglon = lambda prod: print("{:52} | {:10}".format(*prod))

def imprimir(productos):
    """ Imprime la lista de productos """
    imp_linea()
    imp_renglon(("PRODUCTO", "PRECIO"))
    imp_linea()
    for prod in productos:
        imp_renglon(prod)
    imp_linea()

# Par de funciones lambda que lee y valida una respuesta de Si/No, si la
# respuesta si Si regresa True, en otro caso regresa False.
valida_sino = lambda resp: True if resp.lower() in ["si", "s"] else False
lee_sino = lambda msg: valida_sino(input(msg + " "))


def lee_producto(msg):
    """ Lee un producto desde la entrada estándar """
    resp = input(msg + " ")
    print()
    if resp == "":
        # Tenemos respuesta vía, entonce regresamos una tupla vacía
        return tuple()
    else:
        # Tenemos entonces un producto, separamos y pasamos el precio de
        # str a float
        resp = resp.split(",")
        resp[1] = float(resp[1])
        # regresamos la tupla
        return tuple(resp)

# Imprime los mensaje de error
imprime_error = lambda msg: print("{}\n".format(msg))

# Agrega un producto a la lista
agrega = lambda prod: productos.append(producto)

# Ordena la lista de productos
ordena_productos = lambda: productos.sort()

# INICIAR AQUÍ!
while True:  # Se adicionan productos hasta que el usuario ya no quiera
    # 1. Imprimir la lista de productos actual
    imprimir(productos)

    # 2. Preguntar si se desea agregar un producto
    if not lee_sino("Desea agregar un nuevo producto (Si/No)?"):
        break # Hemos terminado

    # 3. SI, leer nombre y precio del nuevo producto
    producto = lee_producto("Escribe nuevo producto (nombre, precio):")

    # 4. Agregar el nuevo producto a la lista de productos
    if producto:
        # si tenemos un producto lo agregamos
        agrega(producto)
        ordena_productos()
    else:
        # si no, enviamos un mensaje de error:
        imprime_error("Producto inválido!")

    # 6. Regresar al paso 1.

