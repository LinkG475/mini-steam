

Lista_Juegos = []
categorias = ["Acción", "Aventura", "Deportes", "Estrategia", "Simulación"]

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


def agregar_juego(lista_juegos):
    codigo_juego = input("Ingrese el código del juego: ")
    nombre_juego = input("Ingrese el nombre del juego: ")
    categoria_juego = input("Ingrese el género del juego: ")
    precio_juego = float(input("Ingrese la plataforma del juego: "))
    #calificacion_juego = ("Ingrese la calificación del juego(1-10): ")
    lista_juegos.append({
        "codigo": codigo_juego,
        "nombre": nombre_juego,
        "categoria": categoria_juego,
        "precio": precio_juego,
#       "calificacion": calificacion_juego
    })

    print("Juego agregado exitosamente.")

def editar_juego(lista_juegos):
    codigo_juego = input("Ingrese el código del juego a editar: ")
    for juego in lista_juegos:
        if juego["codigo"] == codigo_juego:
            print("Juego encontrado. Ingrese los nuevos datos.")
            juego["nombre"] = input("Ingrese el nuevo nombre del juego: ")
            juego["categoria"] = input("Ingrese el nuevo género del juego: ")
            juego["precio"] = input("Ingrese la nueva plataforma del juego: ")
            #juego["calificacion"] = input("Ingrese la nueva calificación del juego(1-10): ")
            print("Juego editado exitosamente.")
            return
    print("Juego no encontrado.")

def eliminar_juego(lista_juegos):
    codigo_juego = input("Ingrese el codigo del juego a eliminar: ")
    for juego in lista_juegos:
        if juego["codigo"] == codigo_juego:
            lista_juegos.remove(juego)
            print("Juego eliminado exitosamente.")
            return
    print("Juego no encontrado.")


def buscar_juego(lista_juegos):
    codigo_juego = input("Ingrese el código del juego a buscar: ")
    for juego in lista_juegos:
        if juego["codigo"] == codigo_juego:
            print(f"Juego encontrado: {juego}")
            return
    print("Juego no encontrado.")

def filtrar_juegos(lista_juegos):
    print("Categorias disponibles:")
    for categoria in categorias:
        print(f"- {categoria}")
    categoria_filtro = input("Ingrese la categoría por la que desea filtrar: ")
    juegos_filtrados = [juego for juego in lista_juegos if juego["categoria"].lower() == categoria_filtro.lower()]
    if juegos_filtrados:
        print("Juegos filtrados:")
        for juego in juegos_filtrados:
            print(juego)
    else:
        print("No se encontraron juegos en esa categoría.")

def Catalogo_Juegos(lista_juegos):
    if not lista_juegos:
        print("No hay juegos disponibles.")
    else:
        print("Catálogo de Juegos:")
        for juego in lista_juegos:
            print(juego)

menu_administrador()
