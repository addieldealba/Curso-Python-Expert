#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from modelosqlite3 import *

BD = "facturas.sqlite3"

@click.group()
def crud():
    parametros_bd(BD)

@crud.command()
@click.argument("razon-social")
@click.argument("rfc")
def c_cliente(razon_social, rfc):
    """ Inserta un registro en la tabla Cliente """
    # Variables que definen que insertar y en que tabla se insertan
    tabla = "Cliente"
    valores = (razon_social, rfc)
    # Se realiza la inserción del registro
    inserta_registro(tabla, valores)

    # Se muestra un mensaje al usuario
    print("Se ha insertado el registro {} en la tabla {}".format(
        valores, tabla))

def imprime_texto(registros):
    """ Imprime la lista de registros en la salida estándar en formato texto """
    # Se obtiene el ancho máximo de cada columna
    anchos = [[len(str(c)) for c in f] for f in registros]
    anchos = [max(f) for f in zip(*anchos)]

    # Se imprime la tabla de resultados
    for fila in registros:
        # Se remplaza los campos vaciós por cademas vacías.
        fila = [c if c != None else "" for c in fila]
        # A cada campo se agrega el valor del ancho
        fila = tuple(zip(fila, anchos))
        # A cada campo se le dá formato
        fila = ["{:{}}".format(*c) for c in fila]
        # Se fusionan los campos en una cadena y se imprimen
        print(" | ".join(fila))

@crud.command()
def r_cliente():
    """ Imprime la lista de registros de la tabla Cliente """
    # Se obtiene la lista de registros de la tabla Autor
    registros = obtiene_registros("Cliente")
    # Se imprimen los registros en formato texto en la salida estándar
    imprime_texto(registros)

@crud.command()
@click.argument("id")
@click.argument("campo")
@click.argument("valor")
def u_cliente(id, campo, valor):
    """ Actualiza los datos de un Cliente """
    # Variables necesarias para actualizar un campo en un registro
    tabla = "Cliente"
    valores = (valor, id)
    actualiza_registro(tabla, campo, valores)

    # Se muestra un mensaje al usuario
    print("Se ha actualizado el registro {} en la tabla {}".format(id, tabla))

@crud.command()
@click.argument("id")
def d_cliente(id):
    """ Elimina un registro de un Cliente """
    # Variables necesarias para eliminar un campo en un registro
    tabla = "Cliente"
    valores = (id,)
    elimina_registro(tabla, valores)

    # Se muestra un mensaje al usuario
    print("Se ha eliminado el registro {} en la tabla {}".format(id, tabla))


if __name__ == '__main__':
    crud()
