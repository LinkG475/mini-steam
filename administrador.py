# Funciones del Administrador
from ambos import mostrar_catalogo, buscar_juego
Catalogo_Juegos = {}  # Diccionario de almacenaje de datos de los juegos
categorias = ["Accion", "Aventura", "Deportes", "Estrategia", "Simulacion"]  
# Codigo de funcion que despliega el menu del administrador después de ingresar la contraseña correcta
def menu_administrador(Catalogo_Juegos):
    while True:
        print("\n--- MENÚ DE ADMINISTRADOR ---")
        print("1. Agregar juego")
        print("2. Editar juego")
        print("3. Eliminar juego")
        print("4. Buscar juego")
        print("5. Mostrar catalogo de juegos")
        print("6. Mostrar codigos de juegos")
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
            mostrar_catalogo(Catalogo_Juegos)
        elif opcion == "6":
            codigos_juegos(Catalogo_Juegos)
        elif opcion == "7":
            print("Regresando a menu inicial...")
            return
        else:
            print("Opción inválida.")
# Codigo de funcion que genera los ID de los juegos dentro del catalogo
def generador_id(Catalogo_Juegos):
    if len(Catalogo_Juegos) == 0:
        codigo = "J001"
        return codigo
    else:
        ultimo = sorted(Catalogo_Juegos.keys())[-1]
        numero = int(ultimo[1:]) + 1
        codigo = f"J{numero:03d}"
        return codigo
# Codigo de funcion para seleccionar la categoria de los juegos dentro del catalogo
def seleccionar_categoria(categorias):
    categoria = input("(Accion, Aventura, Deportes, Estrategia o Simulacion): ")
    while True:
        if categoria.capitalize() in categorias:
            return categoria.capitalize()
        else:
            print("No existe esa categoria.")
            categoria = input("Seleccione una categoria (Accion, Aventura, Deportes, Estrategia o Simulacion): ")
# Codigo de funcion para agregar un juego
def agregar_juego(Catalogo_Juegos):
    codigo_juego = generador_id(Catalogo_Juegos)
    nombre_juego = input("Ingrese el nombre del juego: ")
    print("Seleccione la categoria", end=" ")
    categoria_juego = seleccionar_categoria(categorias)
    while True:
        try:
            precio_juego = float(input("Ingrese el precio del juego: "))
        except ValueError:
            print("El valor no puede ser procesado. Ingrese unicamente numeros.")
        else:
            break
    juego = {
        codigo_juego: {
            "nombre": nombre_juego,
            "categoria": categoria_juego,
            "precio": precio_juego
        }
    }

    Catalogo_Juegos.update(juego)
    print("Juego agregado exitosamente.")
# Codigo de funcion para editar un juego
def editar_juego(Catalogo_Juegos):
    verificacion = 0
    if len(Catalogo_Juegos) == 0:
        print("No hay juegos disponibles.")
    else:
        codigo_juego = input("Ingrese el código del juego a editar: ")
        for codigo, juego in Catalogo_Juegos.items():
            if codigo == codigo_juego.capitalize():
                verificacion = 1
                print("Juego encontrado. Ingrese los nuevos datos.")
                juego["nombre"] = input("Ingrese el nuevo nombre del juego: ")
                print("Seleccione la nueva categoria", end=" ")
                juego["categoria"] = seleccionar_categoria(categorias)
                while True:
                    try:
                        juego["precio"] = float(input("Ingrese el precio del juego: "))
                    except ValueError:
                        print("El valor no puede ser procesado. Ingrese unicamente numeros.")
                    else:
                        break
                print("Juego editado exitosamente.")
                break

        if verificacion == 0:
            print("Juego no encontrado.")
# Codigo de funcion para eliminar un juego
def eliminar_juego(Catalogo_Juegos):
    codigo_juego = input("Ingrese el codigo del juego a eliminar: ")
    for codigo in list(Catalogo_Juegos.keys()):
        if codigo == codigo_juego.capitalize():
            Catalogo_Juegos.pop(codigo)
            print("Juego eliminado exitosamente.")
            return

    print("Juego no encontrado.")
# Codigo de funcion para ver el codigo de los juegos
def codigos_juegos(Catalogo_Juegos):
    if len(Catalogo_Juegos) == 0:
        print("No hay juegos disponibles.")
    else:
        print("Catálogo de Juegos:")
        for codigo, juego in Catalogo_Juegos.items():
            print(f"-{codigo} : {juego["nombre"]}")