#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Micro API JSON de archivos

Métodos:

GET /archivos   Muestra la lista de archivos de la carpeta donde se ejecuta el servidor  en formato JSON
GET /archivos/carpeta
                Muestra la lista de archivos de carpeta en formato JSON
"""

# Desde el módulo bottle sólo se van importando los elemementos que se
# van usando.
from bottle import route, run, template, response
from utilerias import archivos as arch

# Se define la ruta relacionada con la url http://localhost/archivos
@route("/archivos")
@route("/archivos/<directorio>")
def archivos(directorio="."):
    """
    Vista que regresa la lista de archivos de la carpeta donde se ejecuta
    este script en formato json.
    """
    # Constantes definidas por omisión
    # directorio = "."
    # Se obtiene la lista de archivos
    lista = arch.obtiene_archivos(directorio)

    # Se crea un documento en formato json
    doc_json = arch.crea_json(lista)

    # Se define el tipo de contenido
    response.content_type = "application/json"

    return doc_json


# Se carga e inicia el servidor en locahlost en el puerto 8080 y además
# cuando se realiza una modificación en el código en automático reinicia
# el servidor.
run(host="localhost", port=8080, reloader=True)


