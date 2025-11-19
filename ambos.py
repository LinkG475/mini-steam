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

def catalogo_juegos(lista_juegos):
    if not lista_juegos:
        print("No hay juegos disponibles.")
    else:
        print("Catálogo de Juegos:")
        for juego in lista_juegos:
            print(juego)