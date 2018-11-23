#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Modifica el script productos-subtotales.py para que imprima una línea
adicional en la tabla con el total que corresponde a la suma de todos
los subtotales.

"""

# Se crea una variable productos de tipo lista que contendrá todos los
# productos.
productos = [
# Se crea un diccionario por cada producto y contendrá:
# Nombre, Precio y Descuento del producto en porciento.
    {"Nombre":"Automóvil", "Precio":150000.00, "Descuento":0},
    {"Nombre":"Bicicleta", "Precio":13000.00, "Descuento":0},
    {"Nombre":"Chamarra", "Precio":3999.99, "Descuento":0},
    {"Nombre":"Laptop Thinkpad", "Precio":25000.00, "Descuento":13},
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

# Se agrega el nombre de la columna a los títulos de forma manual
titulos.append("SUBTOTAL")

# Se imprime el encabezado 
print("-" * 79)
print("{:40} | {:10} | {:10} | {:10}".format(*titulos))
print("-" * 79)

# Se imprimen los productos
# Observar que type(productos) es list
#              type(producto) es dict
# Se inicia la variable total con 0
total = 0
for producto in productos:
    subtotal = producto["Precio"] * (1 + producto["Descuento"] / 100)
    if len(producto["Nombre"]) > 40:
        print("{:36.36} ... | {:10.2f} | {:10.2f} | {:10.2f} ".format(
        *producto.values(), subtotal))
    else:
        print("{:40.40} | {:10.2f} | {:10.2f} | {:10.2f} ".format(
        *producto.values(), subtotal))
    total += subtotal  # Se acumula el subtotal de cada valor

print("-" * 79)

# Se agrega otro renglón a la tabla
print("{:>66} | {:10.2f} ".format("Total:", total))
print("-" * 79)

