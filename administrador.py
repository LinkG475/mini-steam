# Administrador
from ambos import mostrar_catalogo, filtrar_juegos, buscar_juego
Catalogo_Juegos = {}
categorias = ["Acción", "Aventura", "Deportes", "Estrategia", "Simulación"]

def menu_administrador():
    while True:
        print("\n--- MENÚ DE ADMINISTRADOR ---")
        print("1. Agregar juego")
        print("2. Editar juego")
        print("3. Eliminar juego")
        print("4. Buscar juego")
        print("5. Filtrar juegos")
        print("6. Mostrar catalogo de juegos")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_juego(Catalogo_Juegos)
        elif opcion == "2":
            editar_juego(Catalogo_Juegos)
        elif opcion == "3":
            eliminar_juego(Catalogo_Juegos)
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

def generador_id(Catalogo_Juegos):
    if len(Catalogo_Juegos) == 0:
        codigo = "J001"
        return(codigo)
    else:
        ultimo = sorted(Catalogo_Juegos.keys())[-1]
        numero = int(ultimo[1:]) + 1
        codigo = f"J{numero:03d}"
        return(codigo)
    #Opcion 2
"""if len(Lista_Juegos) == 0:
        codigo = "J001"
    else:
        if len(Lista_Juegos) < 9:
            codigo = f"J00{len(Lista_Juegos)+1}"
        elif len(lista_libros) < 99:
            codigo = f"J0{len(Lista_Juegos)+1}"
        elif len(Lista_Juegos) < 999:
            codigo = f"J{len(Lista_Juegos)+1}"""

def agregar_juego(Catalogo_Juegos):
    codigo_juego = generador_id(Catalogo_Juegos)
    nombre_juego = input("Ingrese el nombre del juego: ")
    categoria_juego = input("Ingrese la categoria del juego: ")
    plataforma = input("Ingrese la plataforma del juego: ")
    precio_juego = float(input("Ingrese el precio del juego: "))
    #calificacion_juego = ("Ingrese la calificación del juego(1-10): ")
    juego = {codigo_juego:
        {"nombre": nombre_juego,
        "categoria": categoria_juego,
        "plataforma" : plataforma,
        "precio": precio_juego}}
#       "calificacion": calificacion_juego}    })
    Catalogo_Juegos.update(juego)
    print("Juego agregado exitosamente.")
    #print(Catalogo_Juegos)

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
                    juego["plataforma"] = input("Ingrese la nueva plataforma del juego: ")
                    juego["precio"] = float(input("Ingrese el nuevo precio del juego: "))         
                    print("Juego editado exitosamente.")
                    print(Catalogo_Juegos)
        if verificacion == 0:
            print("Juego no encontrado.")
#juego["calificacion"] = input("Ingrese la nueva calificación del juego(1-10): ")

def eliminar_juego(Catalogo_Juegos):
    codigo_juego = input("Ingrese el codigo del juego a eliminar: ")
    for juego in Catalogo_Juegos:
        if juego["codigo"] == codigo_juego:
            Catalogo_Juegos.remove(juego)
            print("Juego eliminado exitosamente.")
            return
    print("Juego no encontrado.")


menu_administrador()