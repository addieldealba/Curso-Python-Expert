#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Imprimir una lista de 5 productos en la salida estándar en forma tabular
incluyendo el nombre del producto y su precio.
"""

producto1 = "Automóvil"
precio1 = 150000.00
producto2 = "Bicicleta"
precio2 = 13000.00
producto3 = "Chamarra"
precio3 = 3999.99
producto4 = "Laptop Thinkpad"
precio4 = 25000.00
descuento4 = 13  # dado en por ciento
producto5 = "Gafas de realidad virtual Lenovo con sable laser"
precio5 = 5000.00

print("-" * 65)
print("{:50} | {:10}".format("PRODUCTO", "PRECIO"))
print("-" * 65)
print("{:50} | {:10.2f}".format(producto1, precio1))
print("{:50} | {:10.2f}".format(producto2, precio2))
print("{:50} | {:10.2f}".format(producto3, precio3))
print("{:50} | {:10.2f}".format(
    producto4 + " (Descuento incluido)", precio4 - (descuento4 / 100 * precio4)))
print("{:50} | {:10.2f}".format(producto5, precio5))
print("-" * 65)

