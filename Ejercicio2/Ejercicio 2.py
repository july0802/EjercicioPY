usuarios = {"admin": "admin123"}


def registrar_usuario():
    print("\n--- Registro de nuevo usuario ---")
    nuevo_usuario = input("Ingrese un nombre de usuario: ")
    if nuevo_usuario in usuarios:
        print("El nombre de usuario ya existe. Intente con otro.")
    else:
        nueva_contraseña = input("Ingrese una contraseña: ")
        usuarios[nuevo_usuario] = nueva_contraseña
        print(f"Usuario '{nuevo_usuario}' registrado con éxito.\n")

def iniciar_sesion():
    print("\n--- Inicio de Sesión ---")
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")

    if usuario in usuarios and usuarios[usuario] == contraseña:
        print(f"Bienvenido {usuario}, has iniciado sesión con éxito.\n")
        mostrar_menu()
    else:
        print("Usuario o contraseña incorrectos. Inténtelo nuevamente.\n")

def mostrar_menu():
    while True:
        print("Menú:")
        print("1. Ver Perfil")
        print("2. Configuración")
        print("3. Cerrar Sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Perfil de Usuario")
        elif opcion == "2":
            print("Configuración de Usuario")
        elif opcion == "3":
            print("Cerrando sesión...\n")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.\n")


def main():
    while True:
        print("--- Bienvenido ---")
        print("1. Iniciar Sesión")
        print("2. Registrarse")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            iniciar_sesion()
        elif opcion == "2":
            registrar_usuario()
        elif opcion == "3":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtelo nuevamente.\n")

main()
