#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Sintaxis:
    parametros.py <parámetros...>

Descripción:
El script deberá de leer uno o más parámetros e imprimirlos en la salida
estándar haciendo uso del módulo sys.
"""

import sys

def main(argv):
    """ función principal del script """
    print(argv)


### INICIAR AQUÍ ###
if __name__ == "__main__":
    main(sys.argv)
    # main(sys.argv[1:])


