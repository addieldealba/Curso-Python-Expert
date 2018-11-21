#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Imprimir en la salida estándar un triángulo cuya base es de longitud
n y centrado a lo ancho de la terminal usando ciclos y además
preguntando al inicio el valor de n que tiene que ser un valor entero
positivo e impar mayor o igual a 3.
"""

# Se importa el módulo con nombre sys
import sys

# Se usa el código creado para el script lee-edad.py
n = input("Longitud de la base del triángulo n = ")
# Verificamos si es un entero, positivo y mayor o igual a 3
if n.isdigit() and int(n) >= 3:
    n = int(n)  # Convetimos de str a int
    # Si es par imprimos mensaje de error y terminamos
    if n % 2 == 0:
        print("La longitud tiene que ser un valor impar")
        # Terminamos el script en este punto
        sys.exit()
else:
    print("Error: {} no es un valor adecuado para la longitud".format(n))
    # Como hay un error, aquí terminamos el script
    sys.exit()

# Si el valor de n es adecuado, entonces continuamos

s = "#"  # El símbolo usando para el triángulo
ancho = 54  # Es el ancho de la terminal

print()  # Dejamos una línea en blanco al inicio

# Iniciamos la línea con una cadena vacía
linea = ""

# Iniciamos el ciclo para crear la línea e imprimirla
for i in range(1, n+1, 2):  # Repite para i en [1, 3, 5, ..., n]
    linea = s * i  # Siempre se agregan dos śimbolos por simetría 
    print("{:^{}}".format(linea, n).center(ancho))

print()  # Dejamos una línea en blanco al final

