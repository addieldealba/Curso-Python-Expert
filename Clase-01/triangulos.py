#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Imprimir en la salida estándar un triángulo cuya base es de longitud
n y centrado a lo ancho de la terminal.
"""

n = 9  # La longitud de la base n
s = "#"  # El símbolo usando para el triángulo
ancho = 54  # Es el ancho de la terminal

print()  # Dejamos una línea en blanco al inicio
linea = s  # Creamos nuestra primer línea con sólo un símbolo
print("{:^{}}".format(linea, n).center(ancho))
linea = linea + s * 2  # Siempre agregamos dos símbolos por simetría
print("{:^{}}".format(linea, n).center(ancho))
linea = linea + s * 2  # Seguimos agreando mientras linea sea < n 
print("{:^{}}".format(linea, n).center(ancho))
linea = linea + s * 2  # Seguimos agreando mientras linea sea < n 
print("{:^{}}".format(linea, n).center(ancho))
linea = linea + s * 2  # Seguimos agreando mientras linea sea < n 
print("{:^{}}".format(linea, n).center(ancho))
# Como linea ya tiene 9 símbolos hasta aqí terminamos

print()
