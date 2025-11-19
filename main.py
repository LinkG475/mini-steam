# Main
#from administrador import 
#from usuarios import 
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
            menu_usuario(lista_juegos)
        elif opcion == "2":
            menu_administrador(lista_juegos)
        elif opcion == "3":
            print("Saliendo del programa...")
            break


ejercuion()