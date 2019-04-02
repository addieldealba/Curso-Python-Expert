#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import sqlite3

BD = "biblioteca.sqlite3"

@click.group()
def crud():
    pass


def inserta_registro(tabla, valores):
    """ Inserta un registros en tabla """
    with sqlite3.connect(BD) as conn:
        # Se obtiene un cursor o indice a la base de datos
        cur = conn.cursor()
        # Se arma una tupla con los valores de los campos
        # Se crea una cadena con tantos signos de interrogación como valores
        # tengamos separados por comas
        signos = ", ".join(["?"] * len(valores))
        # Se crea la consulta en SQL
        sql = "insert into {} values (null, {})".format(tabla, signos)
        # Se ejecuta la consulta
        cur.execute(sql, valores)
        # Se ejecuta un commit para indicar que la inserción se ejecute como una
        # operación atómica.
        conn.commit()


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

def obtiene_registros(tabla):
    """
    Obtiene la lista de registros de tabla y los regresa en forma de lista
    """
    # Se realiza la conexión a la base de datos y with la cierra en automático
    with sqlite3.connect(BD) as conn:
        # Se obtiene un cursor o indice a la base de datos
        cur = conn.cursor()
        # Se crea la consulta SQL
        sql = "select * from {}".format(tabla)
        # Se ejecuta la consulta
        cur.execute(sql)
        # Se obtiene la lista de campos y se agrega como primer posición en la
        # lista de resultados.
        registros = [[r[0] for r in cur.description]]
        # Se obtiene la lista de resultados de la consulta SQL
        registros += cur.fetchall()

    return registros

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
    tabla = "Autor"
    # Se realiza la conexión a la base de datos
    with sqlite3.connect(BD) as conn:
        # Se obtiene un cursor o indice a la base de datos
        cur = conn.cursor()
        # Se crea la consulta SQL
        sql = "update {} set {}=? where id{}=?".format(tabla, campo, tabla)
        # Se crea la tupla de valores
        valores = (valor, id)
        # Se ejecuta la consulta SQL agregando los valores de forma segura
        cur.execute(sql, valores)
        # Se ejecuta un commit para indicar a la BD que la actualización se
        # ejecute como una operación atómica.
        conn.commit()

    # Se muestra un mensaje al usuario
    print("Se ha actualizado el registro {} en la tabla {}".format(id, tabla))


@crud.command()
@click.argument("id")
def d_autor(id):
    """ Elimina un registro de un Autor """
    tabla = "Autor"
    # Se realiza la conexión a la base de datos
    with sqlite3.connect(BD) as conn:
        # Se obtiene un cursor o indice a la base de datos
        cur = conn.cursor()
        # Se crea la consulta SQL
        sql = "delete from {} where id{}=?".format(tabla, tabla)
        # Se crea la tupla de valores
        valores = (id,)
        # Se ejecuta la consulta SQL agregando los valores de forma segura
        cur.execute(sql, valores)
        # Se ejecuta un commit para indicar a la BD que la aliminación se
        # ejecute como una operación atómica.
        conn.commit()

    # Se muestra un mensaje al usuario
    print("Se ha eliminado el registro {} en la tabla {}".format(id, tabla))


if __name__ == '__main__':
    crud()
