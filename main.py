# Main
#from administrador import 
from usuarios import pedir_juego, comprar_juego, menu_usuario
from ambos import buscar_juego, filtrar_juegos, mostrar_catalogo

catalogo_juegos = []
contrasenia = "admin123"

def ejecucion():
    while True:
        print("\n--- MENÚ INICIAL ---")
        print("1. Entrar como usuario")
        print("2. Entrar como administrador")
        print("3. Finalizar ejecucion")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_usuario(catalogo_juegos)
            print("Entraste como usuario")
            menu_usuario(lista_juegos)
        elif opcion == "2":
            contra = input("Ingrese la contraseña de administrador: ")
            if contra == contrasenia:
                print("Acceso concedido. Bienvenido ADMINISTRADOR.")
                menu_administrador(catalogo_juegos)
            else:
                print("Contraseña incorrecta. Acceso denegado.")
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no valida.")

ejecucion()