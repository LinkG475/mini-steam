# Main
from administrador import menu_administrador, agregar_juego, editar_juego, eliminar_juego
from usuarios import menu_usuario, pedir_juego, comprar_juego, calificar_juego
from ambos import buscar_juego, filtrar_juegos, catalogo_juegos

Catalogo_Juegos = []
contrasenia = "admin123"
categorias = ["Acción", "Aventura", "Deportes", "Estrategia", "Simulación"]

def ejecucion():
    while True:
        print("\n--- MENÚ INICIAL ---")
        print("1. Entrar como usuario")
        print("2. Entrar como administrador")
        print("3. Finalizar ejecucion")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_usuario(Catalogo_Juegos)
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

ejecucion()