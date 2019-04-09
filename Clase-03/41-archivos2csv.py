#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
El script deberá de crear el archivo archivos.csv con:
- La lista de archivos del directorio actual
- Ordenarlos en base al tamaño en bytes, los más grandes primero
- Incluir sólo los archivos con extensión .py
- Hacer uso de funciones para separar la lógica de la vista y el modelo
- Hacer uso de una clase Archivo.
- El script se debe poder usar como módulo
- Hacer uso de los módulos os y csv de la librería estándar de Python
- Hacer uso del módulo archivos de nuestro paquete utilerias
"""

from utilerias import archivos
import os


def main():
    """ Función pincipal del script """
    # Se obtiene la lista de archivos del directorio actual
    lista_archivos = archivos.obtiene_archivos()

    # Se dejan sólo los archivos con extensión py
    lista_archivos = [a for a in lista_archivos
            if os.path.splitext(a.nombre)[1] == ".py"]
    # Se guarda la lista en archivos.csv 
    archivos.guardar_archivos(lista_archivos)


### INICIAR AQUÍ ###
if __name__ == "__main__":
    main()

