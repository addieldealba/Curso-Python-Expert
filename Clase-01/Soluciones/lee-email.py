#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Leer una email desde la entrada estándar (teclado) e imprime un mensaje
indicando si es o no una dirección de correo válida.
"""

print()

# La función input() (raw_input() en Python2) permite leer los datos
# que escribe el usuario por medio del teclado o entrada estándar.
# Entre paŕentesis se escribe el mensaje que se desea mostrar al
# usuario.
valor = input("Escribe tu e-mail: ")

# Una forma de como validar que es un valor es un e-mail es considerando
# que si es un e-mail desde el inicio e ir descartando poco a poco que
# no lo sea.

# Asumimos que si es un e-mail
es_email = True

# Si tiene @ ?
if "@" not in valor:
    # Si el @ no está en valor entonces no es un e-mail
    es_email = False
if "." not in valor:
    es_email = False
# Si un símbolo $ está en el valor entonces tampoco es un e-mail
if "$" in valor:
    es_email = False

# Hasta aquí ya sabemos si es un e-mail o no
if es_email:
    print("La dirección {} es una dirección e-mail válida".format(valor))
else:
    print("La dirección {} no es una dirección e-mail válida".format(valor))

print()

