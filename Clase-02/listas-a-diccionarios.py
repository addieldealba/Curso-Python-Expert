#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Usar el script productos-con-listas-de-listas.py como base y agregar
código para convertir la lista de listas a una lista de diccionarios
usando ciclos 

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

# Se crea una lista de diccionarios a partir de la lista de listas
productos_dict = []  # Esto es una lista y sus elementos serán dict()
llaves = ["NOMBRE", "PRECIO", "DESCUENTO"]
for producto in productos:
    productos_dict.append(dict(zip(llaves, producto)))
    # La función zip() lo que hace es crear parejas de datos, tomando
    # un dato de llaves y otro dato de producto y esquivalente al
    # siguiente código:
    # lista_parejas = []
    # for i in range(len(llaves)):
    #     lista_parejas.append((llaves[i], producto[i]))
    # 

# Se inicia la impresión de la tabla
print("-" * 65)
print("{:50} | {:10}".format(*llaves))
print("-" * 65)

# Se hace uso de los ciclos for para imprimir los productos
for producto in productos_dict:
    # Si hay un valor de descuento lo hacemos diferente 
    if "DESCUENTO" in producto:
        precio = producto["PRECIO"]
        precio -= producto["DESCUENTO"] / 100 * producto["PRECIO"]
        print("{:50} | {:10.2f}".format(producto["NOMBRE"], precio))
    else:
        print("{:50} | {:10.2f}".format(*producto.values()))

print("-" * 65)

