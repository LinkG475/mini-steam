# Usuarios
from ambos import mostrar_catalogo, filtrar_juegos, buscar_juego
Catalogo_Juegos = {}
Wishlist = []
categorias = ["Acción", "Aventura", "Deportes", "Estrategia", "Simulación"]
Compras = []

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

def comprar_juego(Wishlist, Compras):
    nombre_juego_por_comprar = input("Ingrese el nombre del juego que desea comprar: ")
    for juego in Wishlist:
        if juego["juego"] == nombre_juego_por_comprar:
            confirmación = input(f"{juego["juego"]} cuesta {juego["precio"]} ¿Desea confirmar la compra? (si/no): ")
            while True:
                if confirmación.lower()== "si":
                    print(f"Usted ha comprado: {juego["juego"]}")
                    Compras.append(juego)
                    Wishlist.remove(juego)
                    return
                elif confirmación.lower() == "no":
                    print("Compra cancelada.")
                    return
                else:
                    confirmación = input("Opción invalida. Ingrese si o no: ")
    print("Su juego no ha sido encontrado en su Wishlist.")

def calificar_juego():
    print()

def menu_usuario(Catalogo_Juegos):
    while True:
        print("\n--- MENÚ DE USUARIO ---")
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
            calificar_juego(Catalogo_Juegos)
        elif opcion == "4":
            buscar_juego(Catalogo_Juegos)
        elif opcion == "5":
            filtrar_juegos(Catalogo_Juegos)
        elif opcion == "6":
            mostrar_catalogo(Catalogo_Juegos)
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")
