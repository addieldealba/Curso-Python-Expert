#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Usar script productos-con-listas-de-listas.py agregar uno o dos registro
duplicados y luego hacer uso de conjuntos para eliminarlos.

"""

# Se crea una lista de listas con todos los productos en la variable
# llamada productos
productos = [
    ["Automóvil", 150000.00],
    ["Bicicleta", 13000.00],
    ["Chamarra", 3999.99],
    ["Laptop Thinkpad", 25000.00, 13],
    ["Gafas de realidad virtual Lenovo con sable laser", 5000.00],
    ["Bicicleta", 13000.00],
    ["Laptop Thinkpad", 25000.00, 13],
    ["Laptop Thinkpad", 25000.00, 13],
]

# Se ordena la lista por nombre para observar de forma simple los
# productos repetidos
productos.sort()

# Se convierte a conjunto la lista de productos, eliminando así los
# duplicados, pero recordar que los conjuntos no pueden contener listas
# porque son mutables, así que primero creamos una lista auxiliar donde
# cada producto es una tupla
auxiliar = []
for producto in productos:
    auxiliar.append(tuple(producto))
auxiliar = set(auxiliar)

# Como los conjuntos no son ordenado ahora se convierte a lista
# nuevamente para ordenar los productos restantes de nuevos.
productos = list(auxiliar)
productos.sort()

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

