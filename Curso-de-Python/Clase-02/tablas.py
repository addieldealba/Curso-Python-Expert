#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Este script debe contener una función llamada tabla_del_3() y lo que
hace es imprimir la tabla de multiplicar del 3, sin embargo sólo deberá
estar la definición de la función y nunca deberá ser llamada la función.

"""

# Definición de funciones lambda
linea = lambda: print("-" * 13)
tres_por = lambda n: "3 x {:2} = {:2}".format(n, 3 * n)
renglones_del_3 = lambda: print("\n".join([tres_por(i) for i in range(1, 11)]))

def tabla_del_3():
    """ Imprime la tabla del 3 """

    # INICIAR AQUÍ! Uso de funciones lambda
    print("TABLA DEL 3")
    linea()
    renglones_del_3()
    linea()

