#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Modificar el script nota-de-venta.py para hacer uso de paquetes, módulos
funciones, funciones lambda, listas de compresión y estructuras de datos.

"""

from notas import entrada, salida

# INICIAR AQUÍ
def main():
    """
    Función principal encargada de realizar el flujo principal del
    programa.
    """

    # Se lee si el usuario desea o no iva desglozado
    con_iva = entrada.leesino("Desea iva desglosado (Si/No) ? ")
    # Se inicaliza la lista de productos usando lista de tuplas
    productos = entrada.inicia_productos()

    # función lambda para calcular el subtotal de un producto, donde
    # producto[1] es el precio y producto[2] es la cantidad
    subtotal = lambda producto: producto[1] * producto[2]

    # Se agrega el subtotal a cada tupla de todos los productos, notar
    # la forma de crear una tupla de un sólo elemento.
    productos = [p+(subtotal(p),) for p in productos]

    # Se calcula el total usando listas de compresión y la función
    # sum(), notar que el subtotal está en en índice 3.
    total = sum([p[3] for p in productos])

    # Se imprime la tabla de productos en base a la respuesta del
    # usuario
    print(con_iva)
    salida.imprime(productos, total, con_iva)


# Hacemos que el script se pueda usar como módulo también
if __name__ == "__main__":
    main()

