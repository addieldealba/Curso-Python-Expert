#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import datetime
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

@crud.command()
@click.argument("nombre")
@click.argument("precio", type=float)
@click.argument("cantidad", type=int)
def c_producto(nombre, precio, cantidad):
    """ Inserta un registro en la tabla Producto """
    # Variables que definen que insertar y en que tabla se insertan
    tabla = "Producto"
    valores = (nombre, precio, cantidad)
    # Se realiza la inserción del registro
    inserta_registro(tabla, valores)

    # Se muestra un mensaje al usuario
    print("Se ha insertado el registro {} en la tabla {}".format(
        valores, tabla))

@crud.command()
@click.argument("lugar")
@click.argument("rfcemisor")
@click.argument("idcliente", type=int)
@click.argument("idproducto", type=int)
def c_factura(lugar, rfcemisor, idcliente, idproducto):
    """ Inserta un registro en la tabla Factura """
    # Variables que definen que insertar y en que tabla se insertan
    tabla = "Factura"
    fecha = datetime.datetime.today()  # Fecha de hoy en type datetime
    fecha = fecha.isoformat()  # Fecha de hoy en tipo str en formato iso
    valores = (fecha, lugar, rfcemisor, idcliente, idproducto)
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
