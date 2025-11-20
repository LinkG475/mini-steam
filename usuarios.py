# Usuarios
from ambos import mostrar_catalogo, filtrar_juegos, buscar_juego
Catalogo_Juegos = {}
Wishlist = []
categorias = ["Acción", "Aventura", "Deportes", "Estrategia", "Simulación"]

def pedir_juego(Catalogo_Juegos):
    nombre_juego = input("Ingrese el nombre del juego que desea: ")
    for v in Catalogo_Juegos.values():
        if nombre_juego  == v["nombre"]: 
            precio = v.get("precio")
            juego = {"juego": nombre_juego, "precio": f"${precio:.2f}"}
            Wishlist.append(juego)
            print("El juego solicitado ha sido guardado en la Wishlist.")
            return
    print("El juego no está disponible en el catálogo.")

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

def menu_usuario(Catalogo_Juegos):
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
            pedir_juego(Catalogo_Juegos)
        elif opcion == "2":
            comprar_juego(Catalogo_Juegos)
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")
