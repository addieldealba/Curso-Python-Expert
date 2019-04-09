#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Modifica el script adicionar-productos.py para que imprima el precio
total después de haber terminado de adicionar los nuevos productos.

"""

# Se crea una lista de listas con todos los productos en la variable
# llamada productos
productos = [
    ["Automóvil", 150000.00],
    ["Bicicleta", 13000.00],
    ["Chamarra", 3999.99]
]

# Al inicio el fin es falso porque queremos seguir leyendo más productos
es_fin = False

# Ciclo que permite adicionar tanto productos como queramos
while not es_fin:
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

    # Se lee el nuevo producto
    print()
    resp = input("Capturar nuevo producto (nombre, precio): ")
    if resp == "":
        # Si la respuesta es vacía, entonces terminamos
        es_fin = True
    else:
        # Si hay un producto, entonces lo adicionamos
        producto = resp.split(",")
        producto[1] = float(producto[1])

        # Se agrega a la lista de productos
        productos.append(producto)

        # Se ordena la lista de productos
        productos.sort()

# Calculando el total
total = 0
for producto in productos:
    total += producto[1]

print("-" * 65)
print("El costo total de los productos es:".rjust(50)
        + " | {:10.2f}".format(total))
print("-" * 65)
