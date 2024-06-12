from conexion.conexion import create_connection, close_connection
from funciones.login import Login
import hashlib
from funciones.areasCrud import *
from funciones.tipoTicketsCrud import *
from funciones.usuariosfunciones import *

def menu_jefemesa():
    while True:
        print("\nMenú Jefe de Mesa")
        print("1. Manejar Usuarios")
        print("2. Manejar Áreas")
        print("3. Manejar Tipos de Tickets")
        print("4. Volver al menú anterior")

        choice = input("Seleccione una opción: ")
        if choice == '1':
            usuarios_admin = MantenedorUsuarios()
            usuarios_admin.menu_users()
        elif choice == '2':
            menu_crud_area()
        elif choice == '3':
            menu_tipo_ticket()
        elif choice == '4':
            break
        else:
            print("Opción no válida, intente de nuevo")

def main():
    print("Iniciando función main()...")
    cnx = create_connection()
    if cnx is None:
        print("No se pudo establecer conexión con la base de datos")
        return
    else:
        print("Conexión a la base de datos establecida exitosamente")

    login_instance = Login(cnx)

    intentos = 1
    verificar = False

    while intentos <= 3 and not verificar:
        print("-*-" * 25)
        print("Login de Usuario")
        print("-*-" * 25)

        nombre = input("Ingrese nombre: ")
        contraseña = input("Ingrese Password: ")

        verificar = login_instance.verificar_usuario(nombre, contraseña)

        if verificar:
            print("Inicio de sesión correcto")
            print("-*-" * 25)
            print("Sistema de creación de tiquets")
            print("-*-" * 25)

            tipo = login_instance.verificar_tipo(nombre)
            print(f"Tipo de usuario obtenido: {tipo}")
            
            if tipo == 1:
                print("Mostrar menú jefe de mesa")
                menu_jefemesa()
            elif tipo == 2:
                print("Mostrar menú ejecutivo de área")
            elif tipo == 3:
                print("Mostrar menú ejecutivo de mesa")
        else:
            print("Usuario o contraseña incorrecta. Solo tiene 3 oportunidades, intente nuevamente")
            intentos += 1

    close_connection(cnx)
    print("Conexión a la base de datos cerrada")

if __name__ == "__main__":
    print("Entrando al bloque if __name__ == '__main__':")
    main()
