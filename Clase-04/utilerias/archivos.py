#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

MÓDULO: archivos

Contiene funciones que permiten realizar operaciones con el sistema de
archivos del sistema operativo.

"""

import csv
import datetime
import json
import os


class Archivo:
    """ Se define la clase para el objeto Archivo """
    def __init__(self, nombre, tamanio, fecha, es_dir=None):
        """
        Contructor de la clase con los atributos nombre del archivo,
        tamanio en bytes, fecha en timestamp o en datetime y una bandera
        que indica si es directorio o no.
        """
        self.nombre = nombre
        self.tamanio = tamanio
        if type(fecha) == float or type(fecha) == int:
            self.fecha = datetime.datetime.fromtimestamp(fecha)
        else:
            self.fecha = fecha
        self.es_dir = es_dir

    @property
    def row(self):
        """
        Regresa una lista de los atributos a incluir en una línea de
        un archivo csv
        """
        lista = [self.nombre, self.tamanio,
            self.fecha.strftime("%b %d %Y %H:%M")]
        lista += [self.es_dir] if self.es_dir != None else []

        return lista

    def dict(self):
        """
        Regresa un diccionario de los atributos
        """
        darch = {
            "nombre":self.nombre,
            "tamanio":self.tamanio,
            "fecha":self.fecha.strftime("%b %d %Y %H:%M")
            }
        if self.es_dir != None:
            darch["es_dir"] = self.es_dir

        return darch

    def html_tr(self):
        """
        Regresa una lista de los atributos en formato html haciendo uso
        de la etiqueta <tr>
        """
        return "<tr><td>{}</td><td>{}</td><td>{}</td></tr>".format(
            self.nombre, self.tamanio, self.fecha)

# Imprime una línea horizontal de longitud l
linea = lambda l: print("-" * l)

def obtiene_archivos(d):
    """
    Obtiene la lista de archivos del directorio d y regresa la lista
    ordenada en base al tamaño en bytes del mayor al menor.
    """
    # Se obtiene la lista de archivos usando el módulo os
    archivos = os.listdir(d)

    # Se obtiene el tamaño en bytes y la fecha de modificación usando
    # el módulo os.path y se crea un objeto Archivo
    archivos = [
        Archivo(
            a,
            os.path.getsize(os.path.join(d,a)),
            os.path.getmtime(os.path.join(d,a)),
            os.path.isdir(os.path.join(d,a))
        )
        for a in archivos
    ]

    # Se ordena la lista en base al tamaño
    archivos.sort(key=lambda a: a.tamanio, reverse=True)

    return archivos

# Imprime la lista de archivo en forma de tabla
imprime = lambda archivos: print("\n".join(["{:40} {:10} {:20}".format(*a.row)
    for a in archivos]))

def guardar_archivos(lista, agregar=False, archivo="archivos.csv"):
    """
    Guarda la lista en archivos.csv donde cada elemento debe contar
    una representación en str.
    """
    # Se define el ancho máximo de cada línea en el archivo
    maxcols = 80
    if agregar:
        modo = "a"
    else:
        modo = "w"

    with open(archivo, modo) as fcsv:
        # Se crea un escritor de tipo csv
        csv_writer = csv.writer(fcsv)
        # Guarda cada archivo
        for archivo in lista:
            csv_writer.writerow(archivo.row)


# Imprime la lista de archivo en formato HTML
html = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <link rel="stylesheet" href="main.css">
<head>
<body>
  <h2>Lista de archivos de la carpeta {carpeta}</h2>
  <hr />
  <table>
    <tr><th>Nombre</th><th>Tamaño</th><th>Fecha</th></tr>
    {filas}
  </table>
</body>
</html>
"""
def crea_html(archivos, directorio):
    """ Crea la lista en formato HTML """
    filas = [a.html_tr() for a in archivos]
    datos = {
        "carpeta":directorio,
        "filas":"\n".join(filas)
    }
    return html.format(**datos)
    

def crea_json(archivos):
    """ Crea la lista en formato JSON """
    filas = [a.dict() for a in archivos]
    return json.dumps(filas, indent=4)
    

def guardar(documento, nomarch):
    """
    Guarda el documento en nomarch donde documento está en str
    """
    # Se define el ancho máximo de cada línea en el archivo
    with open(nomarch, "w") as farch:
        farch.write(documento)

def main():
    """ Función principal que se ejecuta cuando es usado como script """

    archivos = obtiene_archivos()
    linea(51)
    imprime(archivos)
    linea(51)


# Las siguiente línea se ejecutan sólo cuando la variable interna de
# Python __name__ es igual a __main__, lo que significa que el script es
# el programa principal y por lo tanto se puede ejecutar la función
# main().
if __name__ == "__main__":
    main()

