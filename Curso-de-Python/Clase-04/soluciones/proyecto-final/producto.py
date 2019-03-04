#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Define la clase Producto así como las funciones y constantes auxilares
para este objeto.
"""

import csv
import os
import shutil

# Se define la clase Producto() con atributos: nombre, cantidad y precio
class Producto:
    """ Se define el objeto Producto """
    def __init__(self, id, nombre, cantidad, precio, imagen=""):
        """ Se define el constructor de la clase """

        # Se inicializan los atributos
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.imagen = imagen

    @property
    def precio_str(self):
        """ Regresa el precio en formato moneda """
        return "{:.2f}".format(self.precio)

    def list(self):
        """
        Regresa un Producto como una lista con todos los atributos
        """
        return [self.id, self.nombre, self.cantidad, self.precio,
                self.imagen]

    def dict(self):
        """ Regresa un Producto en forma de un diccionario """
        return {
            "id":self.id,
            "nombre":self.nombre,
            "cantidad":self.cantidad,
            "precio":self.precio,
            "imagen":self.imagen
        }


def obtiene_productos_csv(nomarch):
    """
    Regresa la lista de productos donde cada elemento es de tipo Producto
    leídos desde el archivo nomarch
    """
    productos = []
    with open(nomarch) as fcsv:
        csv_reader = csv.reader(fcsv)
        for fila in csv_reader:
            producto = Producto(int(fila[0]), fila[1], int(fila[2]),
                    float(fila[3]), fila[4])
            productos.append(producto)

    return productos


def guarda_producto_imagen(img_origen, dir_imagenes, img_destino):
    """ Guarda una copia de img_origen en dir_imagenes/img_destino """
    # Se verifica si dir_imagenes existe, si no se crea
    if not os.path.exists(dir_imagenes):
        os.mkdir(dir_imagenes)

    # Se copia el archivo
    img_destino = os.path.join(dir_imagenes, img_destino)
    shutil.copy(img_origen, img_destino)
    print("La imagen {} ha sido copiada en {}".format(
        img_origen, img_destino))


def guarda_producto_csv(producto, nomarch):
    """ Agrega el producto al archivo nomarch en formato CSV """
    with open(nomarch, "a") as fcsv:
        csv_writer = csv.writer(fcsv)
        csv_writer.writerow(producto.list())
    print("El producto {} ha sido guardado en {}".format(
        producto.nombre, nomarch))

