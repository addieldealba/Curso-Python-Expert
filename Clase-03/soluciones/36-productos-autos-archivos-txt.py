#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Guarda la lista de 3 productos con atributos nombre, cantidad y precio y
3 autos con atributos nombre, cantidad, precio, marca y modelo en un
archivo de texto llamado productos.txt haciendo uso de sólo una función
llamada guardar_productos()
"""

import shutil

# Se defina la clase Producto() con atributos: nombre, apellido paterno y
# edad.
class Producto:
    """ Se define el objeto Producto """
    def __init__(self, nombre, cantidad, precio):
        """ Se define el constructor de la clase """

        # Atributos privados por convensión
        self._an = 15  # Ancho de columna nombre
        self._ac = 8   # Ancho de columna cantidad
        self._ap = 10  # Ancho de columna precio
        self._ast = 10 # Ancho de columna subtotal

        # Se inicializan los atributos de la instancia
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    @property
    def subtotal(self):
        """ Calcula el subtotal para cada producto """
        return self.cantidad * self.precio

    def __str__(self):
        """ Función para definir el formato en str de Producto """
        return "{:{}} {:{}} {:{}.2f} {:{}.2f}".format(
            self.nombre, self._an, self.cantidad, self._ac,
            self.precio, self._ap, self.subtotal, self._ast)

    def total_str(self, total):
        """ Función para definir el formato en str del total """
        return "{:>{}} {:{}.2f}".format(
            "Total:", self._an + self._ac + self._ap + 2,
            total, self._ast)



# Se defina la clase Auto() con atributos: marca, modelo
class Auto(Producto):
    """ Se define el objeto Auto """
    def __init__(self, nombre, cantidad, precio, marca, modelo):
        """ Se define el constructor de la clase """

        # Se ejecuta el constructor de la clase padre
        super().__init__(nombre, cantidad, precio)

        # Se modifica el valor de un atributo privado
        self._an = 25

        # Se inicializan los atributos de la clase hija
        self.marca = marca
        self.modelo = modelo

    # Se sobre escribe el método __str__() de la clase padre para
    # mostrar de forma adecuada un Auto en str.
    def __str__(self):
        """ Función para definir el formato en str de Auto """
        nombre = "{} {} ({})".format(self.marca, self.nombre, self.modelo)
        return "{:{}} {:{}} {:{}.2f} {:{}.2f}".format(
            nombre, self._an, self.cantidad, self._ac,
            self.precio, self._ap, self.subtotal, self._ast)

def obtener_productos():
    """ Crea y regresa una lista de objetos de tipo Producto() """

    # Se crea la lista de objetos Producto()
    productos = [
        Producto("Caja chica", 5, 100.0),
        Producto("Caja mediana", 3, 185.0),
        Producto("Caja grande", 1, 299.0)
    ]

    return productos

def obtener_autos():
    """ Crea y regresa una lista de objetos de tipo Auto() """

    # Se crea la lista de objetos Auto()
    autos = [
        Auto("Vocho", 1, 10000.0, "VW", 2000),
        Auto("Cordoba", 1, 185000.0, "Seat", 2010),
        Auto("Camaro", 1, 299000.0, "Chevrolet", 2018)
    ]

    return autos

def imprimir_productos(lista, total):
    """
    Imprime en la salida estándar los productos en lista, donde cada
    elemento debe ser una clase que tenga definido el método __str__()
    """
    cols, lins = shutil.get_terminal_size()
    print("-" * cols)
    for producto in lista:
        print(producto)
    print("-" * cols)

    # Se imprime el total haciendo uso del método total_str(total) ya
    # que la información para el forma ahora vive dentro de la clase
    print(producto.total_str(total))
    print()  # Esto es sólo para dejar una línea en blanco

def guardar_productos(lista, total, agregar=False):
    """
    Guarda en el archivo productos.txt los productos en lista, donde cada
    elemento debe ser una clase que tenga definido el método __str__() y
    total_str().
    """

    # Se define el ancho máximo de cada línea en el archivo
    maxcols = 80

    # Se abre el archivo para escritura usando with y open
    if agregar:
        modo = "a"
    else:
        modo = "w"
    with open("productos.txt", modo) as flista:
        flista.write("-" * maxcols + "\n")
        for producto in lista:
            flista.write(str(producto) + "\n")
        flista.write("-" * maxcols + "\n")

        # Se imprime el total haciendo uso del método total_str(total) ya
        # que la información para el forma ahora vive dentro de la clase
        flista.write(producto.total_str(total) + "\n")

### INICIAR AQUÍ ###
# Se obtiene la lista de productos y autos
lista_productos = obtener_productos()
lista_autos = obtener_autos()

# Se calcula el total usando listas de compresión
total_productos = sum([p.subtotal for p in lista_productos])
total_autos = sum([a.subtotal for a in lista_autos])

# Se hace uso de sólo una función para guardar ambas listas
guardar_productos(lista_productos, total_productos)
guardar_productos(lista_autos, total_autos, agregar=True)


