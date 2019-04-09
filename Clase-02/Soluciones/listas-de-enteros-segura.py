#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Modifica el script listas-de-enteros-funciones.py para al crear la lista
con 50 millones de número o más muestre una advertencia de que el script
podría bloquear el sistema operativo y pedir confirmación al usuario de
si desea o no continuar.

"""

# No inicies a escribir el script desde aquí, ve al final del script e
# inicia donde dice COMENZAR AQUÍ

def lee_entero(msg, adv_limite=None):
    """
    Lee un entero desde la entrada estándar mostrando el mensaje en msg y
    regresando el valor de tipo int.

    Si adv_limite es diferente de None, entonces si el valor leído es igual
    o mayor, entonces se muestra un mensaje de avertencia preguntando al
    usuario si se desea continuar, si si, entonces se regresa el valor del
    entero leído, si no se regresa el valor None.
    """

    # Hacemos un ciclo infinito hasta que se leea un entero
    while True:
        resp = input(msg + " ")
        if resp.isdigit():
            # Tenemos un entero, pero ahora vamos a comprar si rebasa el
            # límite o no
            n = int(resp)
            if n >= adv_limite:
                print()
                print("El número proporcionado podría bloquear su sistema!")
                resp = input("Desea continuar (s/n)? ")
                print()
                if resp.lower() != "s":
                    return None
            return n
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

# Ahora queremos que lee_entero() no mande una advertencia si el valor
# leído es igual o mayor a 50 millones, así que necesitamos indicarle el
# límite a considerar para la advertencia.
n = lee_entero("Cantidad de números enteros a generar?",
        adv_limite=50000000)
# Ahora hay que verificar si podemos crear la lista
if n != None:
    # Si si, entonces creamos e imprimimos la lista
    lista = crea_lista(n)
    print(lista)
else:
    # Si no, entonces sólo informamos
    print("La creación de la lista ha sido cancelada por el usuario!")

