#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Micro API JSON de productos 

Métodos:

GET /productos  Muestra la lista de productos en formato JSON
GET /producto/id
                Muestra el detalle del producto con id en formato JSON
"""

# Desde el módulo bottle sólo se van importando los elemementos que se
# van usando.
from bottle import route, run, template, response
from notas import entrada, salida

# Nombre del archivo csv
NOMCSV = "productos.csv"

# Se define la ruta relacionada con la url http://localhost/productos
@route("/productos")
def productos():
    """
    Regresa la lista de productos en formato json.
    """
    # Se obtiene la lista de productos 
    lista = entrada.obtiene_productos_csv(NOMCSV)

    # Se crea un documento en formato json
    doc_json = salida.genera_json(lista)

    # Se define el tipo de contenido
    response.content_type = "application/json"

    return doc_json


# Se define la ruta relacionada con la url http://localhost/producto/id
@route("/producto/<id>")
def detalle_producto(id):
    """
    Regresa el detalle de un producto en formato json.
    """
    try:
        # Se convierte id a entero
        id = int(id)
        # Se obtiene la lista de productos 
        lista = entrada.obtiene_productos_csv(NOMCSV)
    except ValueError:
        # Si el id no es entero la lista de productos es vacía
        lista = []

    # Se busca el producto con id
    lista = [p for p in lista if p.id == id]

    # Se crea un documento en formato json
    doc_json = salida.genera_json(lista)

    # Se define el tipo de contenido
    response.content_type = "application/json"

    return doc_json


# Se carga e inicia el servidor en locahlost en el puerto 8080 y además
# cuando se realiza una modificación en el código en automático reinicia
# el servidor.
run(host="localhost", port=8080, reloader=True)


