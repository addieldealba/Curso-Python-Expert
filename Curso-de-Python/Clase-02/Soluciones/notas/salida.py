#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

MÓDULO salida
Contiene funciones cuya función tienen que ver con la impresión de
resultados.

"""

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

