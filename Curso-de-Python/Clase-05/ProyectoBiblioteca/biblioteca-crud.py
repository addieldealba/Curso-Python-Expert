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

@crud.command()
@click.argument("codigo")
@click.argument("genero", type=click.Choice(["Mujer", "Hombre"]))
@click.argument("nombre")
@click.argument("ap-paterno")
@click.argument("ap-materno", required=False)
def c_usuario(codigo, nombre, ap_paterno, ap_materno, genero):
    """
    Inserta un registro en la tabla Usuario, si no se cuenta con el CODIGO de
    usuario usar el código generico 000000.
    """
    # Variables que definen que insertar y en que tabla se insertan
    tabla = "Usuario"
    valores = (codigo, nombre, ap_paterno, ap_materno, genero)
    # Se realiza la inserción del registro
    inserta_registro(tabla, valores)

    # Se muestra un mensaje al usuario
    print("Se ha insertado el registro {} en la tabla {}".format(
        valores, tabla))

@crud.command()
@click.argument("codigo")
@click.argument("titulo")
@click.argument("isbn")
@click.argument("numpags", type=int)
@click.argument("editorial")
@click.argument("idautor", type=int)
def c_libro(codigo, titulo, isbn, numpags, editorial, idautor):
    """
    Inserta un registro en la tabla Libro
    """
    # Variables que definen que insertar y en que tabla se insertan
    tabla = "Libro"
    valores = (codigo, titulo, isbn, numpags, editorial, idautor)
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
@click.argument("tabla")
def read(tabla):
    """ Imprime la lista de registros de TABLA """
    # Se obtiene la lista de registros de tabla
    registros = obtiene_registros(tabla)
    # Se imprimen los registros en formato texto en la salida estándar
    imprime_texto(registros)

@crud.command()
@click.argument("tabla")
@click.argument("id")
@click.argument("campo")
@click.argument("valor")
def update(tabla, id, campo, valor):
    """ Actualiza los datos de CAMPO en TABLA con VALOR en el registro ID """
    # Variables necesarias para actualizar un campo en un registro
    valores = (valor, id)
    actualiza_registro(tabla, campo, valores)

    # Se muestra un mensaje al usuario
    print("Se ha actualizado el registro {} en la tabla {}".format(id, tabla))

@crud.command()
@click.argument("tabla")
@click.argument("id")
def delete(tabla, id):
    """ Elimina un registro ID de TABLA """
    # Variables necesarias para eliminar un campo en un registro
    valores = (id,)
    elimina_registro(tabla, valores)

    # Se muestra un mensaje al usuario
    print("Se ha eliminado el registro {} en la tabla {}".format(id, tabla))


if __name__ == '__main__':
    crud()
