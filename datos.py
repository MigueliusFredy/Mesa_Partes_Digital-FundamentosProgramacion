"""Módulo de datos: arreglos paralelos que almacenan los expedientes.

La posición i de cada arreglo corresponde al mismo expediente.
"""

codigos = []
dnis = []
nombres = []
tipos = []
asuntos = []
correos = []
fechas = []

# Lista con todos los arreglos, útil para recorrerlos juntos
TODOS = [codigos, dnis, nombres, tipos, asuntos, correos, fechas]


def total():
    """Retorna la cantidad de expedientes registrados."""
    return len(codigos)


def limpiar():
    """Vacía todos los arreglos (se usa al cargar el archivo y en las pruebas)."""
    for arreglo in TODOS:
        arreglo.clear()
