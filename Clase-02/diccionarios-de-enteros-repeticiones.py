#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

El script deberá generar una lista de 10 000 número enteros aleatorios,
cada número puede estar en el rando de 0 a 99. Posteriormente encontrar
el número de veces que se repite cada número e imprimir la lista
indicando el número ya las veces que se repite.

"""

import random

# Generando la lista de 10 000 números aleatorios
# range(100) genera números en un rando de 0 a 99
# Con la función choices() elegimos k elementos
numeros = random.choices(range(100), k=10000)  # Tenemos 10000 números

# Ahora se buscan las repeticiones
repeticiones = {}  # Se crea un diccionario vacío
# Se usa un ciclo for para obtener cada número de la lista
for n in numeros:
    # Se verifica si n ya está en las llaves, si es así se adiciona uno
    # al contador, de lo contrario se agrega con el valor de 1
    repeticiones[n] = repeticiones.get(n, 0) + 1
    # La línea anterio es equivalente a las siguientes líneas
    # --- inicia equivalencia ---
    # if n in repeticiones.keys():
    #     repeticiones[n] += 1
    # else:
    #     repeticiones[n] = 1
    # --- termina equivalencia ---

# Se busca el valor máximo de las repeticiones para ajustar la gráfica
maximo = max(repeticiones.values())

# Se imprime la lista de números y sus repeticiones y de forma gráfica
ancho_max = 70  # Es el ancho de la consola / terminal
for llave in sorted(repeticiones.keys()):
    valor = repeticiones[llave]
    long_barra = valor * ancho_max // maximo
    print("{} {} {}".format(llave, "-" * long_barra, valor))


