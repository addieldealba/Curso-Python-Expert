#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Copiar el script productos-con-listas.py con el nombre solicitado y
modificarlo para que todos los productos estén contenidos en una lista
de listas y aprovechar esta nueva variable para imprimir la tabla
haciendo uso del ciclo for.

"""

# Se crea una lista de listas con todos los productos en la variable
# llamada productos
productos = [
    ["Automóvil", 150000.00],
    ["Bicicleta", 13000.00],
    ["Chamarra", 3999.99],
    ["Laptop Thinkpad", 25000.00, 13],
    ["Gafas de realidad virtual Lenovo con sable laser", 5000.00]
]

# Se inicia la impresión de la tabla
print("-" * 65)
print("{:50} | {:10}".format("PRODUCTO", "PRECIO"))
print("-" * 65)

# Se hace uso de los ciclos for para imprimir los productos
for producto in productos:
    # Si hay 3 elementos, el tercero es el descuento
    if len(producto) == 3:
        precio = producto[1] - producto[2] / 100 * producto[1]
        print("{:50} | {:10.2f}".format(producto[0], precio))
    else:
        print("{:50} | {:10.2f}".format(*producto))

print("-" * 65)

