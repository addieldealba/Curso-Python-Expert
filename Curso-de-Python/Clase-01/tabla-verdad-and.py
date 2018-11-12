#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Imprimir la tabla de verdad del operador lógico AND en la salida estándar
en forma tabular incluyendo operador1, operador1 y resultado.
"""

print()
print("{:^40}".format("Tabla de verdad de AND"))
print("-" * 40)
print("{:10} | {:10} | {:9}".format("Operador 1", "Operador 2", "Resultado"))
print("-" * 40)
op1 = True
op2 = True
res = op1 and op2
print("{:10} | {:10} | {:9}".format(str(op1), str(op2), str(res)))
op2 = False
res = op1 and op2
print("{:10} | {:10} | {:9}".format(str(op1), str(op2), str(res)))
op1 = False
op2 = True
res = op1 and op2
print("{:10} | {:10} | {:9}".format(str(op1), str(op2), str(res)))
op2 = False
res = op1 and op2
print("{:10} | {:10} | {:9}".format(str(op1), str(op2), str(res)))
print("-" * 40)