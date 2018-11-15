#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Modifica el script lista-de-productos-total.py para que el total se
calcule usando ciclos

"""

# Lista de productos
producto1 = "Automóvil"
precio1 = 150000.00
cantidad1 = 1
producto2 = "Bicicleta"
precio2 = 13000.00
cantidad2 = 2
producto3 = "Chamarra"
precio3 = 3999.99
cantidad3 = 2
producto4 = "Laptop Thinkpad"
precio4 = 25000.00
cantidad4 = 1
descuento4 = 13  # dado en por ciento
producto5 = "Gafas de realidad virtual Lenovo con sable laser"
precio5 = 5000.00
cantidad5 = 2

# Se imprime la tabla
print("-" * 80)
print("{:48} | {:9} | {:4} | {:9}".format(
    "PRODUCTO", "PRECIO", "CANT", "SUBTOTAL"))
print("-" * 80)
subtotal1 = precio1 * cantidad1
print("{:48} | {:9.2f} | {:4} | {:9.2f}".format(
    producto1, precio1, cantidad1, subtotal1))
subtotal2 = precio2 * cantidad2
print("{:48} | {:9.2f} | {:4} | {:9.2f}".format(
    producto2, precio2, cantidad2, subtotal2))
subtotal3 = precio3 * cantidad3
print("{:48} | {:9.2f} | {:4} | {:9.2f}".format(
    producto3, precio3, cantidad3, subtotal3))
precio4 = precio4 - (descuento4 / 100 * precio4)
subtotal4 = precio4 * cantidad4
print("{:48} | {:9.2f} | {:4} | {:9.2f}".format(
    producto4 + " (Descuento incluido)", precio4, cantidad4, subtotal4))
subtotal5 = precio5 * cantidad5
print("{:48} | {:9.2f} | {:4} | {:9.2f}".format(
    producto5, precio5, cantidad5, subtotal5))
print("-" * 80)

# Se calcula el total por medio de ciclos
# Se inicia el total a cero
total = 0
for i in range(5):  # Se repite el ciclo 5 veces
    # Se obtiene el valor de cada variable subtotali
    total += vars()["subtotal"+str(i+1)]
print("{:>67} | {:9.2f}".format("Total", total))
print("-" * 80)
