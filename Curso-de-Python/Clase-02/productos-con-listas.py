#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Imprimir una lista de 5 productos en la salida estándar en forma tabular
incluyendo el nombre del producto y su precio usando variables de tipo
lista.
"""

# Se crea una lista por cada producto y cada lista contendrá
# Nombre del producto, precio del producto y descuento del producto en
# porciento.
producto1 = ["Automóvil", 150000.00]
producto2 = ["Bicicleta", 13000.00]
producto3 = ["Chamarra", 3999.99]
#             0               , 1       , 2
producto4 = ["Laptop Thinkpad", 25000.00, 13]
producto5 = ["Gafas de realidad virtual Lenovo con sable laser", 5000.00]

# Se inicia la impresión de la tabla
print("-" * 65)
print("{:50} | {:10}".format("PRODUCTO", "PRECIO"))
print("-" * 65)
# Desempacando los elementos de una lista, el siguiente print sería
# equivalente a usar el print de la siguiente forma:
# print("{:50} | {:10.2f}".format("Automóvil", 150000.00))
print("{:50} | {:10.2f}".format(*producto1))
print("{:50} | {:10.2f}".format(*producto2))
print("{:50} | {:10.2f}".format(*producto3))

# Acediendo a elementos individuales de una lista
precio4 = producto4[1] - producto4[2] / 100 * producto4[1]
print("{:50} | {:10.2f}".format(producto4[0], precio4))
print("{:50} | {:10.2f}".format(*producto5))
print("-" * 65)

