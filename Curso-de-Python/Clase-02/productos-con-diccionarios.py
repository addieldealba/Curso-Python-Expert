#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Usar el script productos-con-listas.py como base y modificarlo para usar
diccionarios en lugar de listas para cada variable de un producto.

"""

# Se crea un diccionario por cada producto y contendrá:
# Nombre, Precio y Descuento del producto en porciento.
producto1 = {"Nombre":"Automóvil", "Precio":150000.00, "Descuento":0}
producto2 = {"Nombre":"Bicicleta", "Precio":13000.00, "Descuento":0}
producto3 = {"Nombre":"Chamarra", "Precio":3999.99, "Descuento":0}
producto4 = {"Nombre":"Laptop Thinkpad", "Precio":25000.00, "Dewcuento":13}
producto5 = {
    "Nombre":"Gafas de realidad virtual Lenovo con sable laser",
    "Precio":5000.00,
    "Descuento":0
}

# Se obtienen los títulos de las columnas de las llaves de los
# diccionarios
titulos = []
for t in producto1.keys():
    titulos.append(t.upper())

# Se inicia la impresión de la tabla
print("-" * 76)
print("{:50} | {:10} | {:10}".format(*titulos))
print("-" * 76)
print("{:50} | {:10.2f} | {:10.2f}".format(*producto1.values()))
print("{:50} | {:10.2f} | {:10.2f}".format(*producto2.values()))
print("{:50} | {:10.2f} | {:10.2f}".format(*producto3.values()))
print("{:50} | {:10.2f} | {:10.2f}".format(*producto4.values()))
print("{:50} | {:10.2f} | {:10.2f}".format(*producto5.values()))
print("-" * 76)

