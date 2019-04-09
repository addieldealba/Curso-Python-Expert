#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

El script deberá de crear e imprimir las siguientes listas de números
enteros: lista con 10 números, con 100 números, con 10 000 números, con
100 000 000 números,  con 10 000 000 000 000 000 números.

"""

# Crear e imprimir una lista de 10 números enteros
lista1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista1)
print()

# Sugerencia: Escribir las líneas anteriores y ejecutar hasta aquí

# Crear e imprimir una lista de 100 números enteros
lista2 = list(range(100))
print(lista2)
print()

# Sugerencia: Escribir las líneas anteriores y ejecutar hasta aquí

# RETO: Crear e imprimir una lista de 10 000 números enteros
lista3 = list(range(10000))
print(lista3)
print(len(lista3))
print()

# Sugerencia: Escribir las líneas anteriores y ejecutar hasta aquí

# RETO: Crear e imprimir una lista de 100 000 000 números enteros
# ADVERTENCIA: Esto podría llegar a usar más de 5GB de RAM, si tu equipo
# cuenta con 4GB o menos es casi seguro que el sistema operativo se hirá
# haciendo más lento conforme el script se ejecuta hasta el grado de
# dejar de responder, si eso sucede para el script presionando Ctrl+C.
# Si Ctrl+C ya no responde es posible que tengas que reiniciar tu
# equipo.
#lista4 = list(range(100000000))
#print(lista4)
#print(len(lista4))
#print()

# Sugerencia: Escribir las líneas anteriores y ejecutar hasta aquí

# RETO: Crear e imprimir una lista de 10 000 000 000 000 000 números
# enteros.
# ADVERTENCIA: La ejecución de este script seguramente congelará tu
# sistema operativo, así que tienes que estar preparado para detener el
# script presionando Ctrl+C mientras te sea posible, de lo contrario
# tendrás que reiniciar tu equipo y no importa la cantidad de memoria
# RAM que tengas.
# Para ejecutar el siguiente código tienes que descomentar las líneas
# -------------------------------------------------------------------
# lista5 = []
# i = 0
# while i < 10000000000000000:
#     lista5.append(i)
#     if i % 50000 == 0:  # Se imprime el avance cada 50000
#         print(i)
#     i += 1
# print(lista5)
# print(len(lista5))
# print()
