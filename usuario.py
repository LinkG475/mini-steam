# Funciones del Usuario
from ambos import mostrar_catalogo, filtrar_juegos, buscar_juego
Catalogo_Juegos = {} # Diccionario de almacenaje de datos de los juegos
Wishlist = [] # Lista de juegos deseados por el usuario
categorias = ["Acción", "Aventura", "Deportes", "Estrategia", "Simulación"] 
Compras = [] # Lista de juegos comprados por el usuario

def menu_usuario(Catalogo_Juegos):
    while True:
        print("\n--- MENÚ DE USUARIO ---")
        print("1. Pedir un juego")
        print("2. Comprar juego")
        print("3. Mostrar Wishlist")
        print("4. Revisar juegos comprados")
        print("5. Buscar juego")
        print("6. Filtrar juegos")
        print("7. Mostrar catalogo de juegos")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            pedir_juego(Catalogo_Juegos)
        elif opcion == "2":
            comprar_juego(Wishlist)
        elif opcion == "3":
            mostrar_wishlist(Wishlist)
        elif opcion == "4":
            mostrar_compras(Compras)
        elif opcion == "5":
            buscar_juego(Catalogo_Juegos)
        elif opcion == "6":
            filtrar_juegos(Catalogo_Juegos)
        elif opcion == "7":
            mostrar_catalogo(Catalogo_Juegos)
        elif opcion == "8":
            print("Regresando a menu inicial...")
            return
        else:
            print("Opción inválida.")

def pedir_juego(Catalogo_Juegos):
    nombre_juego = input("Ingrese el nombre del juego que desea: ")
    for v in Catalogo_Juegos.values():
        if nombre_juego  == v["nombre"]: 
            if len(Wishlist) == 0:
                precio = v.get("precio")
                juego = {"juego": nombre_juego, "precio": f"${precio:.2f}"}
                Wishlist.append(juego)
                print("El juego solicitado ha sido guardado en la Wishlist.")
                return
            else:
                for item in Wishlist:
                    if nombre_juego not in item.values():
                        precio = v.get("precio")
                        juego = {"juego": nombre_juego, "precio": f"${precio:.2f}"}
                        Wishlist.append(juego)
                        print("El juego solicitado ha sido guardado en la Wishlist.")
                        return
                    else:
                        print("El juego ya estaba guardado en su Wishlist")
                        return
    print("El juego no está disponible en el catálogo.")

def comprar_juego(Wishlist):
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

def mostrar_wishlist(Wishlist):
    if len(Wishlist) == 0:
        print("No tiene juegos en su Wishlist.")
    else:
        print("Wishlist:")
        for juego in Wishlist:
            print(f"- {juego}")

def mostrar_compras(Compras):
    if len(Compras) == 0:
        print("No ha comprado juegos.")
    else:
        print("Compras:")
        for juego in Compras:
            print(f"- {juego}")

