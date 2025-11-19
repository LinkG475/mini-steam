from ambos import catalogo_juegos, filtrar_juegos, buscar_juego
def pedir_juego():


def comprar_juego():


def menu_usuario():
    while True:
        print("\n--- MENÚ DE USUARIO ---")
        print("1. Pedir juego")
        print("2. Comprar juego")
        print("3. Calificar juego")
        print("4. Mostrar libros")
        print("5. Mostrar estudiantes")
        print("6. Mostrar préstamos")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            pedir_juego(lista_juegos)
        elif opcion == "2":
            comprar_juego(lista_juegos)
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")
