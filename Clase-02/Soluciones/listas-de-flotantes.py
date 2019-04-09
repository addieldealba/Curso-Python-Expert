#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Modifica el script listas-de-enteros.py para que imprima una lista de 50
000 000 (50 millones) de números flotantes distintos.

"""

# Se crea la lista vacía para almacenar todos los numeros de tipo float
lista = []
# Cuanto número vamos a agregar a la lista
n = 50000000

# Se inica el contador i a cero
i = 0

# Mientras el contador i sea menor a n seguimos
while i < n:
    # Creamos nuestro número de tipo float
    num = i + 0.5  # Esto es sólo una forma de resolverlo
    # Agregamos el número a la lista
    lista.append(num)
    # Vamos a imprimir cada 100 000 números, por esa razón usamos el
    # operador del módulo (%), ya que i % 100000 es igual a cero una vez
    # cada 100000 números.
    if i % 100000 == 0:
        print("{} (avance {:.2f}%)".format(i, i / n * 100))
    # Se incrementa en uno el contador i
    i += 1

# Después de construir la lista, se imprime
print(lista)
print(len(lista))
print()
