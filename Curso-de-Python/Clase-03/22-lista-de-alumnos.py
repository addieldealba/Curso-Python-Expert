#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Usar el script lista-personas.py como base para crear la clase hija
Alumno(Persona) que agrega los atributos materia y calificación.
Crear tres alumnos e imprimir la lista.
"""

# Se defina la clase Persona() con atributos: nombre, apellido paterno y
# edad.
class Persona:
    """ Se define el objeto Persona """
    def __init__(self, nombre, a_paterno, edad):
        """ Se define el constructor de la clase """

        # Se inicializan los atributos
        self.nombre = nombre
        self.a_paterno = a_paterno
        self.edad = edad

    @property
    def edad_real(self):
        """ Calcula la edad real de la persona """
        return self.edad + 5

# Se defina la clase Alumno() con atributos: materia y calificacion
class Alumno(Persona):
    """ Se define el objeto Alumno """
    def __init__(self, nombre, a_paterno, edad, materia, calificacion):
        """ Se define el constructor de la clase """

        # Se inicializan los atributos de la clase padre
        super().__init__(nombre, a_paterno, edad)

        # Se inicializan atributos de la clase hija
        self.materia = materia
        self.calificacion = calificacion


def obtener_alumnos():
    """ Crea y regresa una lista de objetos de tipo Alumno() """

    # Se crea la lista de objetos Alumno()
    alumnos = [
        Alumno("Hugo", "Smith", 8, "Curso de Python", 5.9),
        Alumno("Paco", "Lorenz", 28, "Curso de Python", 8.0),
        Alumno("Luis", "Tesla", 38, "Curso de Python", 9.9)
    ]

    return alumnos

def imprimir_alumnos(lista):
    """
    Imprime la lista de alumnos en lista donde cada elemento debe ser
    de tipo Alumno()
    """
    an = 15  # Ancho de columna nombre
    aa = 16  # Ancho de columna a_paterno
    ae = 4   # Ancho de columna edad
    aer = 9  # Ancho de columna edad real
    am = 15  # Ancho de columna materia
    ac = 12  # Ancho de columna calificacion
    at = an + aa + ae + aer + am + ac + 5  # Ancho total

    # Se imprime encabezado
    print("{:{}} {:{}} {:{}} {:{}} {:{}} {:{}}".format("Nombre", an,
        "Apellido", aa, "Edad", ae, "Edad Real", aer, "Materia", am,
        "Calificación", ac))
    # Imprime separador
    print("-" * at)
    # Imprime cada registro de alumnos
    for alumno in lista:
        print("{:{}} {:{}} {:{}} {:{}} {:{}} {:{}}".format(alumno.nombre,
            an, alumno.a_paterno, aa, alumno.edad, ae,
            alumno.edad_real, aer, alumno.materia, am,
            alumno.calificacion, ac))
    # Imprime otro separador
    print("-" * at)

### INICIAR AQUÍ ###
# Se hace uso de una función cuya única tarea es obtener y regresar la
# lista de objetos de tipo Alumno.
lista_alumnos = obtener_alumnos()

# Se hace uso de una función cuya única tarea es imprimir la lista de
# alumnos
imprimir_alumnos(lista_alumnos)

