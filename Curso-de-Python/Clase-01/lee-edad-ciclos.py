#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Modifica el script lee-edad.py para que cuando se proporcione una edad
incorrecta, se vuelva a leer otro valor, continuando así hasta que se
proporcione un valor adecuado de edad.

"""

# Se define que al inicio no tenemos una edad válida usando el valor
# None
edad = None

# Se usa el ciclo while para realizar un ciclo infinito o hasta que se
# teclee una edad válida.
while not edad:  # Mientras no tengamos una edad repetimos
    print()  # Se imprime una línea en blanco

    # Lee un valor desde la entrada estándar
    valor = input("Escribe tu edad: ")

    # Se comprueba que el valor sea una edad
    if valor.isdigit() and int(valor) > 0:
        edad = int(valor)  # Convetimos el valor de str a int
    else:
        print("Error: {} no es un valor adecuado para una edad".format(valor))

# Se imprime el valor de la edad
print("La edad es: {}".format(edad))

print()  # Se imprime una línea en blanco

