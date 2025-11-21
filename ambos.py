# Funciones compartidas
Catalogo_Juegos = {} # Diccionario de almacenaje de datos de los juegos
categorias = ["Acción", "Aventura", "Deportes", "Estrategia", "Simulación"]
# Codigo de funcion para buscar un juego
def buscar_juego(Catalogo_Juegos):
    nombre_juego = input("Ingrese el nombre del juego a buscar: ")
    for juego in Catalogo_Juegos.values():
        if juego["nombre"].upper() == nombre_juego.upper():
            print(f"Juego encontrado:\n - Nombre: {juego["nombre"]}\n - Categoria: {juego["categoria"]} \n - Precio: ${juego["precio"]:.2f}")
            return
    print("Juego no encontrado.")

def filtrar_juegos(Catalogo_Juegos):
    print("Categorias disponibles:")
    for categoria in categorias:
        print(f"- {categoria}")
    categoria_filtro = input("Ingrese la categoría por la que desea filtrar: ")
    juegos_filtrados = [juego for juego in Catalogo_Juegos if juego["categoria"].lower() == categoria_filtro.lower()]
    if juegos_filtrados:
        print("Juegos filtrados:")
        for juego in juegos_filtrados:
            print(juego)
    else:
        print("No se encontraron juegos en esa categoría.")
# Codigo de funcion para mostrar el catalogo de juegos completo
def mostrar_catalogo(Catalogo_Juegos):
    if len(Catalogo_Juegos) == 0:
        print("No hay juegos disponibles.")
    else:
        print("Catálogo de Juegos:")
        for juego in Catalogo_Juegos.values():
            print(juego)