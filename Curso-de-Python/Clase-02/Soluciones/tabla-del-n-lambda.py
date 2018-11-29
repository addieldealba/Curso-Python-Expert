#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Imprimir la tabla del n en la pantalla (salida estándar) usando funciones
lambda para leer n y para crear cada renglón de la tabla. Si es necesario
se puede hacer uso de funciones convencionales.
"""

# Se crea la función lambda para leer un entero
valida = lambda resp: int(resp) if resp.isdigit() else None
lee_entero = lambda msg: valida(input(msg + " "))

# Se crea la tabla
n_por_m = lambda n, m: print("{} x {:2} = {:3}".format(n, m, n * m))
def imprime_tabla_del(n): 
    """ Imprime la tabla del n """
    print("\nTABLA DEL {}".format(n))
    print("-" * 13)
    for i in range(1, 11):
        n_por_m(n, i)
    print("-" * 13)

# COMENZAR AQUÍ!
n = lee_entero("Crea la tabla del n=")
imprime_tabla_del(n)
