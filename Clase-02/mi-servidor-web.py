#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Este script permite mostrar como es posible crear un mini servidor web
usando unas pocas líneas en Python. Después de ejecutar el script
agregar un archivo index.html en la carpeta actual con algo de html y
actualizar el navegador para ver los resultados. Usar el puerto 9000.

"""

import http.server
import socketserver

PUERTO = 9000

# Se crea un controlador que manejará todas las peticiones hacia el
# servidor de tipo http.
controlador = http.server.SimpleHTTPRequestHandler

# Ahora se activa un servicio y se abre o pone en escucha en el puerto
# indicado para recibir las peticiones y pasarlas a nuestro controlador.
# Nuestro servicio de escucha correrá por siempre, por lo que si
# queremos parar el servidor será necesario presionar Control + C
with socketserver.TCPServer(("", PUERTO), controlador) as httpd:
    print("Nuestro servidor está corriendo en http://localhost:{}".format(PUERTO))
    httpd.serve_forever()

