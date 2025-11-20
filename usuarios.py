# Usuarios
from ambos import Catalogo_Juegos, filtrar_juegos, buscar_juego
Lista_Juegos = {}
categorias = ["Acción", "Aventura", "Deportes", "Estrategia", "Simulación"]

def pedir_juego(lista_juegos):
    nombre_juego = input("Ingrese el nombre del juego que desea: ")
    categoria_juego = input("Ingrese la categoría del juego: ")
    if categoria_juego not in categorias:
        print("Categoría no válida. Juego no registrado.")
        return
    if nombre_juego not in lista_juegos:
        print("El juego no está disponible en el catálogo.")
        return
    juego = {"nombre": nombre_juego, "categoria": categoria_juego}
    lista_juegos.append(juego)
    print("Su juego solicitado ha sido registrado.")

def comprar_juego(lista_juegos):
    nombre_juego_por_comprar = input("Ingrese el nombre del juego que desea comprar: ")
    for juego in lista_juegos:
        if juego["nombre"] == nombre_juego_por_comprar.lower():
            print(f"Juego encontrado: {juego}")
        confirmación = input("¿Desea confirmar la compra? (si/no): ")
        if confirmación.lower()== "si":
            print(f"Usted ha comprado el juego: {juego['nombre']}")
        else:
            print("Compra cancelada.")
            return
print("Su juego no ha sido encontrado en el catálogo.")

def calificar_juego():
    print()

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
