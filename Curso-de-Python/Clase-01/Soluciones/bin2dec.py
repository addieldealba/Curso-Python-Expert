#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Este script convertirá un valor en binario a decimal e imprimirá el resultado
en pantalla.
"""

# Se crea una variable con el valor binario
valor_binario = '0b110101'

# Se convierte el valor a decimal usando la función int() y se guarda el valor
# en otra variable.
valor_decimal = int(valor_binario, 2)

# Se imprime el valor binario
print("Valor en binario:", valor_binario)

# Se imprime el valor decimal
print("Valor en decimal:", valor_decimal)