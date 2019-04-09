#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Lee un número entero positivo e imprime su valor multiplicado por 1000
si el valor leído no es un número entero positivo, se deberá mostrar
un mensaje de error.
"""

print()

# La función input() o raw_input() en Python2 permite leer los datos
# que escribe el usuario por medio del teclado o entrada estándar.
# Entre paŕentesis se escribe el mensaje que se desea mostrar al
# usuario.
num = input("Escribe un número entero: ")

# La instrucción if es la instrucción de control más básica y en este
# caso se utiliza para decidir si la variable num es un entero o no.
if num.isdecimal():
    # Si num es un entero lo convertimos de str a int
    num = int(num)
    # Se agrega otra condición para saber si es positivo
    if num > 0:
        # Etnonces es positivo
        print("Resultado:", num * 1000)
    else:
        print("Error: {} es entero, pero no positivo".format(num))
else:
    print("Error: {} no es un entero positivo".format(num))

print()
