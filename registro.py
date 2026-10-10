"""Módulo de registro de expedientes."""
import datos
import validaciones


def generar_codigo(numero):
    """Ejemplo: 7 -> 'EXP-0007'."""
    return "EXP-" + str(numero).zfill(4)


def registrar_expediente(dni, nombre, tipo, asunto, correo, fecha):
    """Registra un expediente si los datos son válidos.

    Retorna el código generado, o None si los datos no son válidos.
    """
    if not validaciones.validar_datos(dni, nombre, tipo, asunto, correo, fecha):
        return None
    codigo = generar_codigo(datos.total() + 1)
    datos.codigos.append(codigo)
    datos.dnis.append(dni)
    datos.nombres.append(nombre.strip())
    datos.tipos.append(tipo.strip())
    datos.asuntos.append(asunto.strip())
    datos.correos.append(correo.strip())
    datos.fechas.append(fecha)
    return codigo


def pedir_y_registrar():
    """Pide los datos por teclado y llama a registrar_expediente()."""
    dni = input("DNI (8 dígitos): ")
    nombre = input("Nombre completo: ")
    tipo = input("Tipo de trámite: ")
    asunto = input("Asunto: ")
    correo = input("Correo electrónico: ")
    fecha = input("Fecha de registro (DD/MM/AAAA): ")
    codigo = registrar_expediente(dni, nombre, tipo, asunto, correo, fecha)
    if codigo is None:
        print("Datos inválidos. El expediente no fue registrado.")
    else:
        print("Expediente registrado. Código de seguimiento:", codigo)
