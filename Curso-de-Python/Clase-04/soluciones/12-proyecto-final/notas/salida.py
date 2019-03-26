#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
MÓDULO salida
Contiene funciones cuya función tienen que ver con la impresión de
resultados.
"""

import csv

def imprime(productos, total, con_iva):
    """ Imprime la lista de productos en forma de tabla """

    print(con_iva)
    # Se imprime el encabezado de la tabla 
    print("-" * 80)
    print("{:48} | {:9} | {:4} | {:9}".format(
        "PRODUCTO", "PRECIO", "CANT", "SUBTOTAL"))
    print("-" * 80)

    # La lista de productos ya incluye el subtotal, así que sólo hay que
    # imprimirlos
    for p in productos:
        print("{:48} | {:9.2f} | {:4} | {:9.2f}".format(*p))

    # Se imprima la línea final
    print("-" * 80)
    # Se gún el usuario eligió
    if not con_iva:
        print("{:>67} | {:9.2f}".format("Total", total))
    else:
        # Si llegamos aquí, el usuario quiere iva
        print("{:>67} | {:9.2f}".format("Subtotal", total))
        print("-" * 80)
        # Calculamos iva y nuevo total
        iva = total * 0.16
        total += iva
        # Se imprime
        print("{:>67} | {:9.2f}".format("IVA", iva))
        print("{:>67} | {:9.2f}".format("Total", total))
        print("-" * 80)


def guarda_producto(producto, nomarch):
    """ Agrega el producto al archivo nomarch en formato CSV """
    with open(nomarch, "a") as fcsv:
        csv_writer = csv.writer(fcsv)
        csv_writer.writerow(producto.row)
    print("El producto {} ha sido guardado en {}!".format(
        producto.nombre, nomarch))


def guarda_nota_csv(lista, subtotal, iva, nomarch):
    """
    Guarda la nota en el archivo nomarch en formato CSV incluyendo el
    desgloce de iva y total.
    """
    with open(nomarch, "w") as fcsv:
        csv_writer = csv.writer(fcsv)

        # Se escribe el encabezado de las columnas
        encabezados = ["Nombre", "Cantidad", "Precio", "Subtotal"]
        csv_writer.writerow(encabezados)

        # Se escriben los productos
        for producto in lista:
            csv_writer.writerow(producto.row)

        # Se escribe el subtotal y desglose de iva
        rsubtotal = [None, None, "Subtotal:", subtotal]
        riva = [None, None, "IVA:", iva]
        rtotal = [None, None, "Total:", subtotal+iva]
        csv_writer.writerow(rsubtotal)
        csv_writer.writerow(riva)
        csv_writer.writerow(rtotal)
    print("Se ha creado la nota de venta en el archivo nota.csv!")

