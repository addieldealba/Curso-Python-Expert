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
    # Se muestra un mensaje al usuario
    print("Se ha insertado el registro {} en la tabla Autor".format(campos))

if __name__ == '__main__':
    crud()
