#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

El script deberá de crear e imprimir la lista de números enteros  con N
elementos, el valor de N será proporcionado por el usuario, por lo que
se sugiere hacer uso de dos funciones.

"""

# No inicies a escribir el script desde aquí, ve al final del script e
# inicia donde dice COMENZAR AQUÍ

def lee_entero(msg):
    """
    Lee un entero desde la entrada estándar mostrando el mensaje en msg y
    regresando el valor de tipo int.
    """

    # Hacemos un ciclo infinito hasta que se leea un entero
    while True:
        resp = input(msg + " ")
        if resp.isdigit():
            # Tenemos un entero
            return int(resp)
        else:
            # Tenemos cualquier cosa, menos un entero
            print()
            print("Error: lo que has escrito no es un entero, intenta de nuevo!")
            print()


def crea_lista(n):
    """
    Crea la lista con n números y la regresa.

    Adicionalmente imprime el avance al ir creando la lista cada 10%
    """

    # Primero se genera la lista
    lista = []
    # Iniciamos nuestro contador
    i = 0

    # Realizamos un ciclo mientras no hayamos llegado a n
    while i < n:
        # Agreganos un número más a la lista
        lista.append(i)
        # Imprimimos avance cada que se ha creado un 10% de la lista
        if i % int(n * 0.1) == 0:
            print("Generando lista al {:2.0f}%".format(i / n * 100))
        # Incrementamos i para pasar al siguiente número
        i += 1

    print()
    # Regresamos la lista completa
    return lista

# COMENZAR AQUÍ: Escribe estás líneas primero
n = lee_entero("Cantidad de números enteros a generar?")
lista = crea_lista(n)
print(lista)

