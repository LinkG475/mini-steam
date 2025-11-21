# Ambos
Catalogo_Juegos = {}
categorias = ["Acción", "Aventura", "Deportes", "Estrategia", "Simulación"]
def buscar_juego(Catalogo_Juegos):
    codigo_juego = input("Ingrese el código del juego a buscar: ")
    for juego in Catalogo_Juegos:
        if juego["codigo"] == codigo_juego.capitalize():
            print(f"Juego encontrado: {juego}")
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

def mostrar_catalogo(Catalogo_Juegos):
    if len(Catalogo_Juegos) == 0:
        print("No hay juegos disponibles.")
    else:
        print("Catálogo de Juegos:")
        for juego in Catalogo_Juegos.values():
            print(juego)