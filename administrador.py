
#Lista de almacenaje de juegos y lista de categorias
Lista_Juegos = []
categorias = ["Acción", "Aventura", "Deportes", "Estrategia", "Simulación"]
#Menu que se despliega al administrador luego de contraseña correcta
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

#codigo de funcion de agregar juego
def agregar_juego(lista_juegos):
    codigo_juego = input("Ingrese el código del juego: ")
    nombre_juego = input("Ingrese el nombre del juego: ")
    categoria_juego = input("Ingrese la categoria del juego: ")
    precio_juego = float(input("Ingrese el precio del juego: "))
    categoria_juego = input("Ingrese el género del juego: ")
    precio_juego = float(input("Ingrese la plataforma del juego: "))
    #calificacion_juego = ("Ingrese la calificación del juego(1-10): ")
    lista_juegos.append({
        "codigo": codigo_juego,
        "nombre": nombre_juego,
        "categoria": categoria_juego,
        "precio": precio_juego})
#       "calificacion": calificacion_juego}    })
    Catalogo_Juegos.update(juego)
        "precio": precio_juego,
#       "calificacion": calificacion_juego
#    })

    print("Juego agregado exitosamente.")
#codigo de funcion de editar juego
def editar_juego(Catalogo_Juegos):
    verificacion = 0
    if len(Catalogo_Juegos) == 0:
        print("No hay juegos disponibles.")
    else:
        codigo_juego = input("Ingrese el código del juego a editar: ")
        for codigo, juego in Catalogo_Juegos.items():
            if codigo == codigo_juego.capitalize():
                verificacion = 1
                if verificacion == 1:    
                    print("Juego encontrado. Ingrese los nuevos datos.")
                    juego["nombre"] = input("Ingrese el nuevo nombre del juego: ")
                    juego["categoria"] = input("Ingrese el nuevo género del juego: ")
                    juego["precio"] = float(input("Ingrese el nuevo precio del juego: "))         
                    print("Juego editado exitosamente.")
        if verificacion == 0:
            print("Juego no encontrado.")
#juego["calificacion"] = input("Ingrese la nueva calificación del juego(1-10): ")
#codigo de funcion de editar juego
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

#codigo de funcion de eliminar juego
def eliminar_juego(lista_juegos):
    codigo_juego = input("Ingrese el codigo del juego a eliminar: ")
    for juego in lista_juegos:
        if juego["codigo"] == codigo_juego:
            lista_juegos.remove(juego)
            print("Juego eliminado exitosamente.")
            return
    print("Juego no encontrado.")


menu_administrador()
#codigo de funcion de buscar juego
def buscar_juego(lista_juegos):
    codigo_juego = input("Ingrese el código del juego a buscar: ")
    for juego in lista_juegos:
        if juego["codigo"] == codigo_juego:
            print(f"Juego encontrado: {juego}")
            return
    print("Juego no encontrado.")

#codigo de funcion de filtrar juegos
def filtrar_juegos(lista_juegos):
    print("Categorias disponibles:")
    for categoria in categorias:
        print(categoria)
    categoria_filtro = input("Ingrese la categoría por la que desea filtrar: ")
    juegos_filtrados = [juego for juego in lista_juegos if juego["categoria"].lower() == categoria_filtro.lower()]
    if juegos_filtrados:
        print("Juegos filtrados:")
        for juego in juegos_filtrados:
            print(juego)
    else:
        print("No se encontraron juegos en esa categoría.")
#Codigo para opcion Catalogo de Juegos
def Catalogo_Juegos(lista_juegos):
    if not lista_juegos:
        print("No hay juegos disponibles.")
    else:
        print("Catálogo de Juegos:")
        for juego in lista_juegos:
            print(juego)

menu_administrador()
