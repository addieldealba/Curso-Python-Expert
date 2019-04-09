#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Imprimir la tabla de verdad del operador lógico NOT en la salida estándar
en forma tabular incluyendo operador1 y resultado.
"""

# Variables que definen las dimensiones de la tabla
ancho_ter = 58  # Ancho de la terminal
ancho_op1 = 10  # Ancho del campo del operador 1
ancho_res = 10  # Ancho del campo de resultado
ancho_tabla = ancho_op1 + 3 + ancho_res  # El ancho de la tabla se calcula

# Se inicia la impresión de la tabla
print()
print("{:^{}}".format(
    "Tabla de verdad de NOT", ancho_tabla).center(ancho_ter))
print(("-" * ancho_tabla).center(ancho_ter))
print("{:{}} | {:{}}".format(
    "Operador 1", ancho_op1, "Resultado", ancho_res).center(ancho_ter))
print(("-" * ancho_tabla).center(ancho_ter))
op1 = True
res = not op1
print("{:{}} | {:{}}".format(
    str(op1), ancho_op1, str(res), ancho_res).center(ancho_ter))
op1 = False
res = not op1
print("{:{}} | {:{}}".format(
    str(op1), ancho_op1, str(res), ancho_res).center(ancho_ter))
print(("-" * ancho_tabla).center(ancho_ter))