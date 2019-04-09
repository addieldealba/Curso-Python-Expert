#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Modificar el script tabla-del-5.py para leer N desde el teclado e
imprimir la tabla del N en la salida estándar usando ciclos.

N tiene que ser un entero positivo mayor o igual a 2, si el valor leído
es incorrecto se muestra un mensaje de error y se termina el script.

"""

# Se importa el módulo sys
import sys

# Se lee N y se comprueba que cumpla los requisitos, de lo contrario
# se imprime un error y se termina el script.
n = input("Escribe el número de la tabla a imprimir n= ")

# Se verifica que sea entero y mayor o igual a 2
if n.isdigit() and int(n) >= 2:
    n = int(n)  # Convetimos de str a int
else:
    print("Error: {} no es un valor adecuado o no es entero".format(n))
    sys.exit()

print()  # Se deja una línea en blanco

# Se imprime el encabezado de la tabla
print("TABLA DEL {}".format(n))
print("-" * 14)

# Se imprimen los renglones del 1 al 10
for i in range(1, 11):  # recordar que range llega hasta 11-1=10
    print("{} x {:2} = {:3}".format(n, i, n * i))

# Se imprime el fin de la tabla
print("-" * 14)

print()  # Se deja una línea en blanco
