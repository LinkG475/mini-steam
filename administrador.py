Lista_Juegos = []

def menu_administrador():
    while True:
        print("\n--- MENÚ DE ADMINISTRADOR ---")
        print("1. Agregar Juego")
        print("2. Editar Juego")
        print("3. Eliminar Juego")
        print("4. Buscar Juego")
        print("5. Filtrar Juegos")
        print("6. Catalogo Juegos")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_juego(Lista_Juegos)
        elif opcion == "2":
            editar_juego(Lista_Juegos)
        elif opcion == "3":
            eliminar_juego(Lista_Juegos)
        elif opcion == "4":
            buscar_juego(Lista_Juegos)
        elif opcion == "5":
            filtrar_juegos(Lista_Juegos)
        elif opcion == "6":
            Catalogo_Juegos(Lista_Juegos)
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")