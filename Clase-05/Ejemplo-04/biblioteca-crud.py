#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import sqlite3

BD = "biblioteca.sqlite3"

@click.group()
def crud():
    pass

@crud.command()
@click.argument("nombre")
@click.argument("ap-paterno")
@click.argument("ap-materno", required=False)
def c_autor(nombre, ap_paterno, ap_materno):
    """ Inserta un registro en la tabla Autor """
    # Se arma una tupla con los campos
    campos = (nombre, ap_paterno, ap_materno)
    # Se realiza la conexión a la base de datos
    conn = sqlite3.connect(BD)
    # Se obtiene un cursor o indice a la base de datos
    cur = conn.cursor()
    # Se ejecuta la consulta SQL colocando un símbolo ? para cada valor de cada
    # campo para evitar inyección SQL. Es la recomendación que hace el módulo
    # sqlite3.
    cur.execute("insert into Autor values (null, ?, ?, ?)", campos)
    # Se ejecuta un commit para indicar que la inserción se ejecute como una
    # operación atómica.
    conn.commit()
    # Se cierra la base de datos
    conn.close()
    # Se muestra un mensaje al usuario
    print("Se ha insertado el registro {} en la tabla Autor".format(campos))

@crud.command()
def r_autor():
    """ Imprime la lista de registros de la tabla Autor """
    # Se realiza la conexión a la base de datos y with la cierra en automático
    with sqlite3.connect(BD) as conn:
        # Se obtiene un cursor o indice a la base de datos
        cur = conn.cursor()
        # Se ejecuta la consulta SQL colocando un símbolo ? para cada valor de
        # cada campo para evitar inyección SQL. Es la recomendación que hace el
        # módulo sqlite3.
        cur.execute("select * from Autor")
        # Se obtiene la lista de campos y se agrega como primer posición en la
        # lista de resultados.
        res = [[r[0] for r in cur.description]]
        # Se obtiene la lista de resultados de la consulta SQL
        res += cur.fetchall()

    # Se obtiene el ancho máximo de cada columna
    anchos = [[len(str(c)) for c in f] for f in res]
    anchos = [max(f) for f in zip(*anchos)]
    # Se imprime la tabla de resultados
    for fila in res:
        # Se remplaza los campos vaciós por cademas vacías.
        fila = [c if c != None else "" for c in fila]
        # A cada campo se agrega el valor del ancho
        fila = tuple(zip(fila, anchos))
        # A cada campo se le dá formato
        fila = ["{:{}}".format(*c) for c in fila]
        # Se fusionan los campos en una cadena y se imprimen
        print(" | ".join(fila))

@crud.command()
@click.argument("idautor")
@click.argument("campo")
@click.argument("valor")
def u_autor(idautor, campo, valor):
    """ Actualiza los datos de un Autor """
    # Se realiza la conexión a la base de datos
    with sqlite3.connect(BD) as conn:
        # Se obtiene un cursor o indice a la base de datos
        cur = conn.cursor()
        # Se crea la consulta SQL
        sql = "update Autor set {}=? where idAutor=?".format(campo)
        # Se crea la tupla de valores
        valores = (valor, idautor)
        # Se ejecuta la consulta SQL agregando los valores de forma segura
        cur.execute(sql, valores)
        # Se ejecuta un commit para indicar a la BD que la actualización se
        # ejecute como una operación atómica.
        conn.commit()

    # Se muestra un mensaje al usuario
    print("Se ha actualizado el registro {} en la tabla Autor".format(idautor))


@crud.command()
@click.argument("idautor")
def d_autor(idautor):
    """ Elimina un registro de un Autor """
    # Se realiza la conexión a la base de datos
    with sqlite3.connect(BD) as conn:
        # Se obtiene un cursor o indice a la base de datos
        cur = conn.cursor()
        # Se crea la consulta SQL
        sql = "delete from Autor where idAutor=?"
        # Se crea la tupla de valores
        valores = (idautor,)
        # Se ejecuta la consulta SQL agregando los valores de forma segura
        cur.execute(sql, valores)
        # Se ejecuta un commit para indicar a la BD que la aliminación se
        # ejecute como una operación atómica.
        conn.commit()

    # Se muestra un mensaje al usuario
    print("Se ha eliminado el registro {} en la tabla Autor".format(idautor))


if __name__ == '__main__':
    crud()
