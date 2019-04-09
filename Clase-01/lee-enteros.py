#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Lee un número entero e imprime su valor multiplicado por 100, si el
valor leído no es un número entero se deberá mostrar un mensaje de
error.
"""

print()

# La función input() o raw_input() en Python2 permite leer los datos
# que escribe el usuario por medio del teclado o entrada estándar.
# Entre paŕentesis se escribe el mensaje que se desea mostrar al
# usuario.
num = input("Escribe un número entero: ")

# La instrucción if es la instrucción de control más básica y en este
# caso se utiliza para decidir si la variable num es un entero o no.
if num.isdigit():
    print("Resultado:", int(num) * 100)
else:
    print("Error: {} no es un entero".format(num))

print()
