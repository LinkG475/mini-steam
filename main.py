# Main
#from administrador import 
from usuarios import pedir_juego, comprar_juego, menu_usuario
from ambos import buscar_juego, filtrar_juegos, mostrar_catalogo

catalogo_juegos = []


def ejecucion():
    while True:
        print("\n--- MENÚ INICIAL ---")
        print("Seleccione su rol:")
        print("1. Usuario")
        print("2. Administrador")
        print("3. Finalizar ejecucion")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_usuario(catalogo_juegos)
        elif opcion == "2":
            menu_administrador(catalogo_juegos)
        elif opcion == "3":
            print("Saliendo del programa...")
            break


ejercuion()