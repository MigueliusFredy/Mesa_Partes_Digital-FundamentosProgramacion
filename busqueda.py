"""Módulo de búsqueda de expedientes (búsqueda secuencial)."""
import datos


def buscar_posicion(codigo_buscado):
    """Retorna la posición del código en el arreglo, o -1 si no existe."""
    i = 0
    posicion = -1
    while i < datos.total() and posicion == -1:
        if datos.codigos[i] == codigo_buscado:
            posicion = i
        else:
            i = i + 1
    return posicion


