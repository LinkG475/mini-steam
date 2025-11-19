# Main
#from administrador import 
#from usuarios import 
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
            print("Entraste como usuario")
            menu_usuario(lista_juegos)
        elif opcion == "2":
            contra = input("Ingrese la contraseña de administrador: ")
            if contra == contrasenia:
                print("Acceso concedido. Bienvenido ADMINISTRADOR.")
            else:
                print("Contraseña incorrecta. Acceso denegado.")
            menu_administrador(lista_juegos)
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no valida.")

ejercuion()