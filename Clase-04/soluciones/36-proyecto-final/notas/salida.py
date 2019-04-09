#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
MÓDULO salida
Contiene funciones cuya función tienen que ver con la impresión de
resultados.
"""

import csv
import json

def genera_txt(productos, total=None, con_iva=None):
    """
    Genera un documento txt con la lista de productos en forma de tabla
    """

    # Se inicia el documento
    doc_txt = ""

    # Todas la líneas se tiene que terminar en \n
    doc_txt += "-" * 80 + "\n"
    doc_txt += "{:48} | {:4} | {:9} | {:9}\n".format(
        "PRODUCTO", "CANT", "PRECIO", "SUBTOTAL")
    doc_txt += "-" * 80 + "\n"

    # Se agrega cada producto al documento
    for p in productos:
        doc_txt += "{:48} | {:4} | {:9.2f} | {:9.2f}\n".format(*p.row)

    doc_txt += "-" * 80 + "\n"

    # Si hay un total se imprime
    if total != None:
        if con_iva != None:
            # Si hay iva se agrega el desgloze de iva

            # Se agrega el subtotal
            doc_txt += "{:>67} | {:9.2f}\n".format("Subtotal", total)
            # Calculamos iva y nuevo total
            iva = total * 0.16
            total += iva
            # Se agrega el iva
            doc_txt += "{:>67} | {:9.2f}\n".format("IVA", iva)

        # Se agrega el total
        doc_txt += "{:>67} | {:9.2f}\n".format("Total", total)

    # Se regresa el documento
    return doc_txt

def genera_html(productos, total=None, con_iva=None):
    """
    Genera un documento html con la lista de productos en forma de tabla
    """

    # Se inicia el documento html a usar como plantilla
    doc_html = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <link rel="stylesheet" href="main.css">
<head>
<body>
  <h2>Lista de productos</h2>
  <hr />
  <table>
    <tr><th>Nombre</th><th>Cantidad</th><th>Precio</th><th>Subtotal</th></tr>
    {filas}
  </table>
</body>
</html>
    """

    # Se define la forma de una fila en html para un producto
    fila_html = "<tr><td>{}</td><td>{}</td><td>{:.2f}</td><td>{:.2f}</td></tr>"
    # Se define la forma de una fila en html para un total
    fila_html_total = "<tr><td>{}</td><td>{}</td><td>{}</td><td>{:.2f}</td></tr>"

    # Se crea una lista, donde cada elemento es una fila en html y datos
    filas = [fila_html.format(*p.row) for p in productos]

    # Si hay un total se agrega 
    if total != None:
        if con_iva != None:
            # Si hay iva se agrega el desgloze de iva

            # Se agrega el subtotal
            filas.append(fila_html_total.format("", "", "Subtotal", total))
            # Calculamos iva y nuevo total
            iva = total * 0.16
            total += iva
            # Se agrega el iva
            filas.append(fila_html_total.format("", "", "IVA", iva))

        # Se agrega el total
        filas.append(fila_html_total.format("", "", "Total", total))

    # Se regresa el documento uniendo las filas en una sola cadena y
    # luego uniéndola con la plantilla.
    return doc_html.format(**{"filas":"\n".join(filas)})

def imprime(productos, total=None, con_iva=None):
    """ Imprime la lista de productos en forma de tabla """

    doc_txt = genera_txt(productos, total, con_iva)

    print(doc_txt)

def imprime_html(productos, total=None, con_iva=None):
    """ Imprime la lista de productos en formato HTML """

    doc_html = genera_html(productos, total, con_iva)

    print(doc_html)

def imprime_json(productos):
    """ Imprime la lista de productos en formato JSON """

    # Se crea una lista de diccionarios, donde cada diccionario
    # representa un producto
    doc_json = json.dumps([p.dict() for p in productos], indent=4)

    print(doc_json)

def guarda(archivo, productos, total=None, con_iva=None):
    """ Guarda la lista de productos en forma de tabla en archivo """

    doc_txt = genera_txt(productos, total, con_iva)

    with open(archivo, "w") as ftxt:
        ftxt.write(doc_txt)

def guarda_html(archivo, productos, total=None, con_iva=None):
    """ Guarda la lista de productos en formato HTML en archivo """

    doc_html = genera_html(productos, total, con_iva)

    with open(archivo, "w") as fhtml:
        fhtml.write(doc_html)


def guarda_json(archivo, productos):
    """ Guarda la lista de productos en formato JSON en archivo """

    with open(archivo, "w") as fjson:
        json.dump([p.dict() for p in productos], fjson, indent=4)


def guarda_producto(producto, nomarch):
    """ Agrega el producto al archivo nomarch en formato CSV """
    with open(nomarch, "a") as fcsv:
        csv_writer = csv.writer(fcsv)
        csv_writer.writerow(producto.row)
    print("El producto {} ha sido guardado en {}!".format(
        producto.nombre, nomarch))


def guarda_nota_csv(lista, subtotal, iva, nomarch):
    """
    Guarda la nota en el archivo nomarch en formato CSV incluyendo el
    desgloce de iva y total.
    """
    with open(nomarch, "w") as fcsv:
        csv_writer = csv.writer(fcsv)

        # Se escribe el encabezado de las columnas
        encabezados = ["Nombre", "Cantidad", "Precio", "Subtotal"]
        csv_writer.writerow(encabezados)

        # Se escriben los productos
        for producto in lista:
            csv_writer.writerow(producto.row)

        # Se escribe el subtotal y desglose de iva
        rsubtotal = [None, None, "Subtotal:", subtotal]
        riva = [None, None, "IVA:", iva]
        rtotal = [None, None, "Total:", subtotal+iva]
        csv_writer.writerow(rsubtotal)
        csv_writer.writerow(riva)
        csv_writer.writerow(rtotal)
    print("Se ha creado la nota de venta en el archivo nota.csv!")

