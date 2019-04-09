#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

El script deberá de crear e imprimir la lista de números enteros  con N
elementos, el valor de N será proporcionado por el usuario, por lo que
se sugiere hacer uso de dos funciones.

"""

import random
import sys

def lee_entero(msg, valor=None):
    """
    Lee un entero desde la entrada estándar mostrando el mensaje en msg y
    regresando el valor de tipo int.

    Si valor es diferente de None se regresa en caso de que el usuario no
    proporcione alguno.
    """

    # Hacemos un ciclo infinito hasta que se leea un entero
    while True:
        resp = input(msg + " ")
        # si la respuesta está vacía regresamos valor
        if resp == "" and valor != None:
            return valor
        # si no, entonces vemos si es un entero
        elif resp.isdigit():
            # Tenemos un entero y lo regresamos
            return int(resp)
        else:
            # Tenemos cualquier cosa, menos un entero
            print()
            print("Error: lo que has escrito no es un entero, intenta de nuevo!")
            print()

def crea_claves(n, m):
    """
    Crea una lista de n claves de m caracteres y la regresa
    """
    # Se definen los símbolos a usar para crear las claves
    minusculas = "abcdefghijklmnopqrstuvwxyz"
    mayusculas = minusculas.upper()
    digitos = "0123456789"

    # Variable para almacenar la lista de m claves
    claves = []
    # Tenemos que generar n claves, así que podemos usar un ciclo for
    for i in range(n):
        # Se inicia una variable para almacenar una clave
        clave = []
        # Se selecciona cuando menos una minúscula, una mayúscula y un digito
        clave.append(random.choice(minusculas))  # Ej. clave = ["a"]
        clave.append(random.choice(mayusculas))  # Ej. clave = ["a","B"]
        clave.append(random.choice(digitos))     # Ej. clave = ["a","B","3"]

        # Nos falta elegir m - 3 caracteres, pero se tiene que elegir del
        # conjunto de minúsculas + mayúsculas + dígitos
        alfabeto = minusculas + mayusculas + digitos  # Suma de cadenas
        clave += random.choices(alfabeto, k=m-3)  # Suma de listas
        # Ej. clave = ["a", "B", "3", "v", "G", "8", "f", "m"] si m = 8

        # Pero la clave siempre inicia con una minúscula, luego una mayúscula y
        # después un dígito porque así la estamos construyendo, por lo tanto hay
        # que desordenar los elementos para darle mayor fortaleza.
        random.shuffle(clave)  # Desordena los elementos una lista

        # Sólo falta imprimir la clave, pero recordar que clave es de tipo
        # lista, pero necesitamos imprimir un cadena, así que la forma de
        # convertir una lista -> cadena es usando la función .join()
        claves.append("".join(clave))

    return claves

# Se hace uso de una función para leer n
n = lee_entero("Número de claves a generar:")

# Se hace uso de una función para leer m y además se indica el valor a
# usar en caso de omisión.
m = lee_entero("Longitud de claves (8):", valor=8)

# Se crean las claves
claves = crea_claves(n, m)

# Se imprimen
for clave in claves:
    print(clave)
