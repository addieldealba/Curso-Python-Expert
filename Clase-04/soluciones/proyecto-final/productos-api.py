#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Micro aplicación web que responderá las siguiente peticiones hacerca de
productos en formato HTML y JSON respectivamente.

Métodos HTML

GET /
GET /productos  Muestra la lista de productos en formato HTML en forma
                tabular incluyendo nombre, cantidad, precio e imagen.
GET /productos/id
                Muestra el detalle del producto con id en formato HTML

Métodos JSON

GET /api/productos
                Regresa un documento json con la lista de productos.
GET /api/productos/id
                Regresa un documento json con el detalle del producto con
                id.
"""

from bottle import route, run, template, response, view, static_file, abort
from producto import Producto, obtiene_productos_csv

import json

# Nombre del archivo csv
NOMCSV = "productos.csv"

# Se define la ruta para los archivos estáticos como css, js o imágenes
@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')

# En este caso particular se definen las imagenes de los productos en una
# carpeta separada.
@route('/imagenes/<filepath>')
def server_imagenes(filepath):
    return static_file(filepath, root='imagenes')


# Se define la ruta relacionada con la url http://localhost/productos
@route("/")
@route("/productos")
@view("productos")
def productos():
    """
    Regresa la lista de productos en formato HTML.
    """
    # Se obtiene la lista de objetos de tipo Producto 
    lista = obtiene_productos_csv(NOMCSV)

    return dict(productos=lista)

# Se define la ruta relacionada con la url http://localhost/productos/id
@route("/productos/<id>")
@view("productos-detalle")
def productos_detalle(id):
    """
    Regresa el detalle de un producto en formato html.
    """
    try:
        # Se convierte id a entero
        id = int(id)
        # Se obtiene la lista de productos 
        lista = obtiene_productos_csv(NOMCSV)
        # Se busca el producto con id
        lista = [p for p in lista if p.id == id]
        try:
            producto = lista[0]
        except IndexError:
            # Si el id no existe no tenemos producto
            abort(404, "Producto no encontrado")
    except ValueError:
        # Si el id no es entero no tenemos producto
        abort(405, "El id de producto no es válido")

    return dict(producto=producto)


# Se define la ruta relacionada con la url http://localhost/api/productos
@route("/api/productos")
def productos_json():
    """
    Regresa la lista de productos en formato json.
    """
    # Se obtiene la lista de productos 
    lista = obtiene_productos_csv(NOMCSV)

    # Se crea un documento en formato json
    doc_json = json.dumps([p.dict() for p in lista], indent=4)

    # Se define el tipo de contenido
    response.content_type = "application/json"

    return doc_json


# Se define la ruta relacionada con la url
# http://localhost/api/productos/id
@route("/api/productos/<id>")
def productos_detalle_json(id):
    """
    Regresa el detalle de un producto en formato json.
    """
    try:
        # Se convierte id a entero
        id = int(id)
        # Se obtiene la lista de productos 
        lista = obtiene_productos_csv(NOMCSV)
        # Se busca el producto con id
        lista = [p for p in lista if p.id == id]
        try:
            producto = lista[0]
            # Se crea un documento en formato json
            doc_json = json.dumps([producto.dict()], indent=4) 
        except IndexError:
            # Si el id no existe no tenemos producto
            doc_json = json.dumps([{
                "codigo":1,
                "descripcion": "Producto no encontrado"
            }], indent=4)
    except ValueError:
        # Si el id no es entero no tenemos producto y se avisa al
        # usuario
        doc_json = json.dumps([{
            "codigo":2,
            "descripcion": "El id de producto no es válido"
        }], indent=4, ensure_ascii=False)


    # Se define el tipo de contenido
    response.content_type = "application/json"

    return doc_json


# Se carga e inicia el servidor en locahlost en el puerto 8080 y además
# cuando se realiza una modificación en el código en automático reinicia
# el servidor.
run(host="0.0.0.0", port=8080, reloader=True)


