# Usuarios
from ambos import catalogo_juegos, filtrar_juegos, buscar_juego
Lista_Juegos = []
categorias = ["Acción", "Aventura", "Deportes", "Estrategia", "Simulación"]

def pedir_juego():


def comprar_juego():


def calificar_juego():
    

def menu_usuario(lista_juegos):
    while True:
        print("\n--- MENÚ DE ADMINISTRADOR ---")
        print("1. Pedir un juego")
        print("2. Comprar juego")
        print("3. Calificar juego")
        print("4. Buscar juego")
        print("5. Filtrar juegos")
        print("6. Mostrar catalogo de juegos")
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
