#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Modificar el script tabla-del-3-lambda.py haciendo uso de exclusivamente
de funciones lambda y listas de compresión para imprimir la tabla.

"""
# Definición de funciones lambda
linea = lambda: print("-" * 13)
tres_por = lambda n: "3 x {:2} = {:2}".format(n, 3 * n)
tabla_del_3 = lambda: print("\n".join([tres_por(i) for i in range(1, 11)]))

# INICIAR AQUÍ! Uso de funciones lambda
print("TABLA DEL 3")
linea()
tabla_del_3()
linea()

