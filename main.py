"""Programa principal: Mesa de Partes Digital."""
import archivos
import registro
import busqueda
import ordenamiento


def mostrar_menu():
    print("\n=== MESA DE PARTES DIGITAL ===")
    print("1. Registrar expediente")
    print("2. Buscar expediente por código")
    print("3. Ordenar expedientes por código")
    print("4. Listar expedientes")
    print("0. Salir")


def main():
    archivos.cargar_archivo()
    opcion = ""
    while opcion != "0":
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()
        if opcion == "1":
            registro.pedir_y_registrar()
        elif opcion == "2":
            busqueda.pedir_y_buscar()
        elif opcion == "3":
            ordenamiento.ordenar_expedientes()
            print("Expedientes ordenados por código.")
        elif opcion == "4":
            ordenamiento.listar_expedientes()
        elif opcion == "0":
            archivos.guardar_archivo()
            print("Datos guardados. Hasta pronto.")
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
