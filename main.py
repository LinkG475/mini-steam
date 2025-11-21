# Main
from administrador import menu_administrador, agregar_juego, editar_juego, eliminar_juego
from usuarios import menu_usuario, pedir_juego, comprar_juego
from ambos import buscar_juego, filtrar_juegos, mostrar_catalogo

Catalogo_Juegos = {}
# Datos de administrador
contrasenia = "admin123"
categorias = ["Acción", "Aventura", "Deportes", "Estrategia", "Simulación"]
# Datos de usuario
Wishlist = []
Compras = []
# Menú de ejecución principal
def ejecucion(Catalogo_Juegos):
    while True:
        print("\n--- MENÚ INICIAL ---")
        print("1. Entrar como usuario")
        print("2. Entrar como administrador")
        print("3. Finalizar ejecucion")

        opcion = input("Seleccione una opción: ")
#Opciones de menu inicial
        if opcion == "1":
            print("Entraste como usuario")
            menu_usuario(Catalogo_Juegos)
        elif opcion == "2":
            contra = input("Ingrese la contraseña de administrador: ")
            if contra == contrasenia:
                print("Acceso concedido. Bienvenido ADMINISTRADOR.")
                menu_administrador(Catalogo_Juegos)
            else:
                print("Contraseña incorrecta. Acceso denegado.")
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no valida.")

ejecucion(Catalogo_Juegos)