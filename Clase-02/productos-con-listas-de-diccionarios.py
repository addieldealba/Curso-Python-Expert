#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Usar el script productos-con-diccionarios.py como base y modificarlo
para usar una lista de diccionarios como variable donde se almacenarán
todos los productos.

"""

# Se crea una variable productos de tipo lista que contendrá todos los
# productos.
productos = [
# Se crea un diccionario por cada producto y contendrá:
# Nombre, Precio y Descuento del producto en porciento.
    {"Nombre":"Automóvil", "Precio":150000.00, "Descuento":0},
    {"Nombre":"Bicicleta", "Precio":13000.00, "Descuento":0},
    {"Nombre":"Chamarra", "Precio":3999.99, "Descuento":0},
    {"Nombre":"Laptop Thinkpad", "Precio":25000.00, "Dewcuento":13},
    {
        "Nombre":"Gafas de realidad virtual Lenovo con sable laser",
        "Precio":5000.00,
        "Descuento":0
    }
]

# Se obtienen los títulos de las columnas a partir de las llaves de
# cualquier producto.
titulos = []
for t in productos[0].keys():
    titulos.append(t.upper())

# Se imprime el encabezado 
print("-" * 76)
print("{:50} | {:10} | {:10}".format(*titulos))
print("-" * 76)

# Se imprimen los productos
# Observar que type(productos) es list
#              type(producto) es dict
for producto in productos:
    print("{:50} | {:10.2f} | {:10.2f}".format(*producto.values()))

print("-" * 76)

