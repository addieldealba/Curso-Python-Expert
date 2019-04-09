#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
El script deberá instanciar 3 personas y 3 alumnos y luego imprimirlos
en una tabla en la salida estándar haciendo uso de sólo una función
imprime_lista()
"""

import shutil

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

    def __str__(self):
        """ Define el formato en str() de Persona() """
        an = 15  # Ancho de columna nombre
        aa = 16  # Ancho de columna a_paterno
        ae = 4   # Ancho de columna edad
        aer = 9  # Ancho de columna edad real

        return "{:{}} {:{}} {:{}} {:{}}".format(self.nombre, an,
                self.a_paterno, aa, self.edad, ae, self.edad_real, aer)


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

    def __str__(self):
        """ Define el formato en str() de Alumno() """
        am = 15  # Ancho de columna materia
        ac = 12  # Ancho de columna calificacion

        # Se hace uso del método __str__() de la clase padre por medio
        # de super()
        return super().__str__() + " {:{}} {:{}}".format(
            self.materia, am, self.calificacion, ac
            )


def obtener_personas():
    """ Crea y regresa una lista de objetos de tipo Persona() """

    # Se crea la lista de objetos Persona()
    personas = [
        Persona("Hugo", "Smith", 8),
        Persona("Paco", "Lorenz", 28),
        Persona("Luis", "Tesla", 38)
    ]

    return personas

def obtener_alumnos():
    """ Crea y regresa una lista de objetos de tipo Alumno() """

    # Se crea la lista de objetos Alumno()
    alumnos = [
        Alumno("Hugo", "Smith", 8, "Curso de Python", 5.9),
        Alumno("Paco", "Lorenz", 28, "Curso de Python", 8.0),
        Alumno("Luis", "Tesla", 38, "Curso de Python", 9.9)
    ]

    return alumnos

def imprimir_lista(lista):
    """
    Imprime la lista en la salida estándar donde cada elemento debe contar
    una representación en str.
    """
    # Encontramos el ancho de la terminal
    cols, lins = shutil.get_terminal_size()
    # Imprime separador
    print("-" * cols)
    # Imprime cada registro
    for registro in lista:
        print(registro)
    # Imprime otro separador
    print("-" * cols)

### INICIAR AQUÍ ###

# Se obtiene la lista de personas y alumnos
lista_personas = obtener_personas()
lista_alumnos = obtener_alumnos()

# Se hace uso de una función cuya única tarea es imprimir la lista
imprimir_lista(lista_personas)
imprimir_lista(lista_alumnos)

