#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from modelosqlite3 import *

BD = "biblioteca.sqlite3"

@click.group()
def crud():
    parametros_bd(BD)

@crud.command()
@click.argument("nombre")
@click.argument("ap-paterno")
@click.argument("ap-materno", required=False)
def c_autor(nombre, ap_paterno, ap_materno):
    """ Inserta un registro en la tabla Autor """
    # Variables que definen que insertar y en que tabla se insertan
    tabla = "Autor"
    valores = (nombre, ap_paterno, ap_materno)
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
def r_autor():
    """ Imprime la lista de registros de la tabla Autor """
    # Se obtiene la lista de registros de la tabla Autor
    registros = obtiene_registros("Autor")
    # Se imprimen los registros en formato texto en la salida estándar
    imprime_texto(registros)

@crud.command()
@click.argument("id")
@click.argument("campo")
@click.argument("valor")
def u_autor(id, campo, valor):
    """ Actualiza los datos de un Autor """
    # Variables necesarias para actualizar un campo en un registro
    tabla = "Autor"
    valores = (valor, id)
    actualiza_registro(tabla, campo, valores)

    # Se muestra un mensaje al usuario
    print("Se ha actualizado el registro {} en la tabla {}".format(id, tabla))

@crud.command()
@click.argument("id")
def d_autor(id):
    """ Elimina un registro de un Autor """
    # Variables necesarias para eliminar un campo en un registro
    tabla = "Autor"
    valores = (id,)
    elimina_registro(tabla, valores)

    # Se muestra un mensaje al usuario
    print("Se ha eliminado el registro {} en la tabla {}".format(id, tabla))


if __name__ == '__main__':
    crud()
