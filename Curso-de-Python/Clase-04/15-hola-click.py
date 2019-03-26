#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click

@click.command()  # Le decimos a click que esta función será un comando
@click.argument("nombre")
@click.argument("n", default=1)
def hola(nombre, n):
    """
    El script deberá de imprimir N veces el mensaje “Hola NOMBRE!” en la
    salida estándar haciendo uso del módulo click.
    """
    for i in range(n):
        print("Hola {}!".format(nombre))



### Iniciar aquí ###

if __name__ == "__main__":
    hola()
