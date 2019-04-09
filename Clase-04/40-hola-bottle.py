#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Mostrar el mensaje Hola NOMBRE! en el navegador accediendo a la url
http://localhost:8000/hola/NOMBRE
"""

# Desde el módulo bottle sólo se van importando los elemementos que se
# van usando.
from bottle import route, run, template

# Se define la ruta relacionada con la url http://localhost/hola/nombre
@route("/hola/<nombre>")
def index(nombre):
    """
    Función o vista que atiende las peticiones de la ruta
    """
    # Se crea una plantilla usando html y la notación {{nombre}}
    # define una variable llamada nombre cuy valor es pasado a la
    # plantilla como segúndo parámetro.
    return template("<h3>Hola {{nombre}}!</h3>", nombre=nombre)

# Se carga e inicia el servidor en locahlost en el puerto 8080 y además
# cuando se realiza una modificación en el código en automático reinicia
# el servidor.
run(host="localhost", port=8080, reloader=True)


