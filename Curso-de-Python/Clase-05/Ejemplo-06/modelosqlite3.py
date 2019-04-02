#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Módulo encargado de realizar las opetaciones a la base de datos SQLite3
"""

import sqlite3

def parametros_bd(bd):
    """ Define los parámetros para realizar la conexión a la BD """
    global BD
    BD = bd

def inserta_registro(tabla, valores):
    """ Inserta un registro en tabla """
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

def actualiza_registro(tabla, campo, valores):
    """ Actualiza un registro en tabla """
    # Se realiza la conexión a la base de datos
    with sqlite3.connect(BD) as conn:
        # Se obtiene un cursor o indice a la base de datos
        cur = conn.cursor()
        # Se crea la consulta SQL
        sql = "update {} set {}=? where id{}=?".format(tabla, campo, tabla)
        # Se crea la tupla de valores
        # Se ejecuta la consulta SQL agregando los valores de forma segura
        cur.execute(sql, valores)
        # Se ejecuta un commit para indicar a la BD que la actualización se
        # ejecute como una operación atómica.
        conn.commit()

def elimina_registro(tabla, valores):
    """ Elimina un registro en tabla """
    # Se realiza la conexión a la base de datos
    with sqlite3.connect(BD) as conn:
        # Se obtiene un cursor o indice a la base de datos
        cur = conn.cursor()
        # Se crea la consulta SQL
        sql = "delete from {} where id{}=?".format(tabla, tabla)
        # Se crea la tupla de valores
        # Se ejecuta la consulta SQL agregando los valores de forma segura
        cur.execute(sql, valores)
        # Se ejecuta un commit para indicar a la BD que la aliminación se
        # ejecute como una operación atómica.
        conn.commit()
