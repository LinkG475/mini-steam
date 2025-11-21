# Funciones compartidas
Catalogo_Juegos = {} # Diccionario de almacenaje de datos de los juegos
categorias = ["Accion", "Aventura", "Deportes", "Estrategia", "Simulacion"]
# Codigo de funcion para buscar un juego
def buscar_juego(Catalogo_Juegos):
    nombre_juego = input("Ingrese el nombre del juego a buscar: ")
    for juego in Catalogo_Juegos.values():
        if juego["nombre"].upper() == nombre_juego.upper():
            print(f"Juego encontrado:\n - Nombre: {juego["nombre"]}\n - Categoria: {juego["categoria"]} \n - Precio: ${juego["precio"]:.2f}")
            return
    print("Juego no encontrado.")
# Codigo de funcion para mostrar el catalogo de juegos completo
def mostrar_catalogo(Catalogo_Juegos):
    if len(Catalogo_Juegos) == 0:
        print("No hay juegos disponibles.")
    else:
        print("Catálogo de Juegos:")
        for juego in Catalogo_Juegos.values():
            print(juego)