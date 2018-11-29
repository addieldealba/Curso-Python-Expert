#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Imprimir la tabla del 3 en la pantalla (salida estándar) usando funciones
lambda para optimizar y simplificar el código.
"""

tres_por = lambda n: print("3 x {:2} = {:2}".format(n, 3 * n))


print("TABLA DEL 3")
print("-" * 13)
tres_por(1)
tres_por(2)
tres_por(3)
tres_por(4)
tres_por(5)
tres_por(6)
tres_por(7)
tres_por(8)
tres_por(9)
tres_por(10)
print("-" * 12)

