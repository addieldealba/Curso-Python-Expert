#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Modificar el script lista-de-productos-total-ciclos.py para preguntar al
usuario si quiere o no el iva desglosado, entonces imprimir la lista de
productos y el total con o sin iva desglosado según corresponda.

El usuario puede responder s, S, Si o SI para el caso afirmativo, n, N,
No o NO para el caso contrario y cualquier otra respuesta se considera
incorrecta por lo que se deberá de volver a preguntar.

"""

# Se lee la respuesta del usuario para elegir si quiere o no iva
# desglosado.
desglose = None
while desglose == None:  # Mientras no tengamos respuesta correcta, seguimos
    print()  # Deja una línea en blanco
    valor = input("Desea iva desglosado (Si/No) ? ")
    if valor.lower() == "s" or valor.lower() == "si":
        desglose = True  # Si queremos iva desglosado
    elif valor.lower() == "n" or valor.lower() == "no":
        desglose = False  # No queremos iva desglosado
    else:
        print("    Error: {} no es una respuesta válida, intenta de nuevo.".
            format(valor))

# Lista de productos
producto1 = "Automóvil"
precio1 = 150000.00
cantidad1 = 1
producto2 = "Bicicleta"
precio2 = 13000.00
cantidad2 = 2
producto3 = "Chamarra"
precio3 = 3999.99
cantidad3 = 2
producto4 = "Laptop Thinkpad"
precio4 = 25000.00
cantidad4 = 1
descuento4 = 13  # dado en por ciento
producto5 = "Gafas de realidad virtual Lenovo con sable laser"
precio5 = 5000.00
cantidad5 = 2

# Se imprime la tabla
print("-" * 80)
print("{:48} | {:9} | {:4} | {:9}".format(
    "PRODUCTO", "PRECIO", "CANT", "SUBTOTAL"))
print("-" * 80)
subtotal1 = precio1 * cantidad1
print("{:48} | {:9.2f} | {:4} | {:9.2f}".format(
    producto1, precio1, cantidad1, subtotal1))
subtotal2 = precio2 * cantidad2
print("{:48} | {:9.2f} | {:4} | {:9.2f}".format(
    producto2, precio2, cantidad2, subtotal2))
subtotal3 = precio3 * cantidad3
print("{:48} | {:9.2f} | {:4} | {:9.2f}".format(
    producto3, precio3, cantidad3, subtotal3))
precio4 = precio4 - (descuento4 / 100 * precio4)
subtotal4 = precio4 * cantidad4
print("{:48} | {:9.2f} | {:4} | {:9.2f}".format(
    producto4 + " (Descuento incluido)", precio4, cantidad4, subtotal4))
subtotal5 = precio5 * cantidad5
print("{:48} | {:9.2f} | {:4} | {:9.2f}".format(
    producto5, precio5, cantidad5, subtotal5))
print("-" * 80)

# Se calcula el total por medio de ciclos
# Se inicia el total a cero
subtotal = 0
for i in range(5):  # Se repite el ciclo 5 veces
    # Se obtiene el valor de cada variable subtotali
    subtotal += vars()["subtotal"+str(i+1)]
# Si hay iva desglosado imprimimos Subtotal en lugar de Total
if desglose:
    print("{:>67} | {:9.2f}".format("Subtotal", subtotal))
else:
    print("{:>67} | {:9.2f}".format("Total", subtotal))
print("-" * 80)

# Si no se quiere iva desglosado, hasta aquí terminamos
if desglose:
    # Calculamos iva y total
    iva = subtotal * 0.16
    total = subtotal + iva
    # Se imprime
    print("{:>67} | {:9.2f}".format("IVA", iva))
    print("{:>67} | {:9.2f}".format("Total", total))
    print("-" * 80)


