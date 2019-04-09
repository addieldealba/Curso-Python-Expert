#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Usar script productos-con-listas-de-listas.py  como base e imprime la
lista de productos ordenadas en base al precio.

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

# Se ordena la lista de productos antes de imprimir
# productos.sort()  # Esto no funciona
# Creamos una lista auxiliar de tuplas, donde el primer elemento es el
# precio
auxiliar = []  # Esta tiene que ser una lista porque vamos a modificarla
for producto in productos:
    auxiliar.append( (producto[1], producto) )
auxiliar.sort()  # Ahora si ordenamos en base al precio

# Se inicia la impresión de la tabla
print("-" * 65)
print("{:50} | {:10}".format("PRODUCTO", "PRECIO"))
print("-" * 65)

# Se utiliza la lista auxiliar y se desempaqueta el producto
for precio, producto in auxiliar:
    # Si hay 3 elementos, el tercero es el descuento
    if len(producto) == 3:
        precio = producto[1] - producto[2] / 100 * producto[1]
        print("{:50} | {:10.2f}".format(producto[0], precio))
    else:
        print("{:50} | {:10.2f}".format(*producto))

print("-" * 65)

