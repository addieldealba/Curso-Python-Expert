#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

El script deberá de crear e imprimir una lista de n claves de longitud
m incluyendo cuando menos una minúscula, una mayúscula y un dígito. Los
valores de n y m serán solicitados al usuario y m deberá tener el valor
de 8 en caso de que el usuario no proporcione ninguno.

Adicionalmente se incluye cuando menos un símbolo como parte de la clave

"""

import random
import sys


# Se lee el valor de n
print()
resp = input("Número de claves a generar: ")
# Se verifica si son digitos o no
if not resp.isdigit():
    print()
    print("Error: el valor no es un entero positivo")
    print()
    sys.exit()  # Terminamos el script ya que no podemos continuar
# Se convierte a entero
n = int(resp)

# Se lee el valor de m
resp = input("Longitud de claves (8): ")
# Se verifica si la respuesta está vacía
if resp == "":
    # Entonces usamos el valor por omisión
    m = 8
# Se verifica si son digitos o no
elif not resp.isdigit():
    print()
    print("Error: el valor no es un entero positivo")
    print()
    sys.exit()  # Terminamos el script ya que no podemos continuar
else:
    # Se convierte a entero
    m = int(resp)

# Se definen los símbolos a usar para crear las claves
minusculas = "abcdefghijklmnopqrstuvwxyz"
mayusculas = minusculas.upper()
digitos = "0123456789"
simbolos = "@#$%&/=-_+*"

print()
# Tenemos que generar n claves, así que podemos usar un ciclo for
for i in range(n):
    # Se inicia una variable para almacenar una clave
    clave = []
    # Se selecciona cuando menos una minúscula, una mayúscula y un digito
    clave.append(random.choice(minusculas))  # Ej. clave = ["a"]
    clave.append(random.choice(mayusculas))  # Ej. clave = ["a","B"]
    clave.append(random.choice(digitos))     # Ej. clave = ["a","B","3"]
    # Se elecciona cuando menos un símbolo
    clave.append(random.choice(simbolos))  # Ej. clave = ["a","B","3", "#"]

    # Nos falta elegir m - 4 caracteres, pero se tiene que elegir del
    # conjunto de minúsculas + mayúsculas + dígitos + simbolos
    alfabeto = minusculas + mayusculas + digitos  # Suma de cadenas
    alfabeto += simbolos  # Seguimos sumando cadenas
    clave += random.choices(alfabeto, k=m-4)  # Suma de listas ¿porqué?
    # Ej. clave = ["a", "B", "3", "#", "G", "8", "f", "m"] si m = 8

    # Pero la clave siempre inicia con una minúscula, luego una
    # mayúscula, después un dígito y luego un símbolo porque así la estamos
    # construyendo, por lo tanto hay que desordenar los elementos para
    # darle mayor fortaleza.
    random.shuffle(clave)  # Desordena los elementos una lista

    # Sólo falta imprimir la clave, pero recordar que clave es de tipo
    # lista, pero necesitamos imprimir un cadena, así que la forma de
    # convertir una lista -> cadena es usando la función .join()
    print("".join(clave))


