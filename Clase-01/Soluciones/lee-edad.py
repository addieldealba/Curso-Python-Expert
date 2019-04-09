#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Leer una valor de edad desde la entrada estándar (teclado) e imprime
un mensaje indicando si es mayor de edad o no. Considerar que una
persona es mayor de edad si tiene 18 o más años cumplidos.

Si el valor leído no es una edad, entonces se imprime un mensaje de
error.
"""

print()

# La función input() (raw_input() en Python2) permite leer los datos
# que escribe el usuario por medio del teclado o entrada estándar.
# Entre paŕentesis se escribe el mensaje que se desea mostrar al
# usuario.
num = input("Escribe tu edad: ")

# Una edad es un número entero positivo, así que sólo basta con que
# veamos que sean puros dígitos y mayor a cero será suficiente.
if num.isdigit() and int(num) > 0:
    num = int(num)  # Convetimos de str a int
    # Para saber si es mayor de edad verificamos si es mayor o igual
    # a 18.
    if num >= 18:
        print("Eres mayor de edad, ya puedes tomar gaseosas!")
    else:
        print("Eres menor de edad, puedes tomar malteadas!")
else:
    print("Error: {} no es un valor adecuado para una edad".format(num))

print()
