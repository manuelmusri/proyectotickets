from ast import main
from conexion.conexion import create_connection, close_connection

def create_tipo_ticket(connection):
    cursor = connection.cursor()
    
    nombre = input("Ingrese el nombre del ticket: ")
    id_jefe = int(input("Ingrese el ID del jefe: "))
    query = "INSERT INTO tipo_ticket ( nombre, id_jefe) VALUES ( %s, %s)"
    cursor.execute(query, ( nombre, id_jefe))
    connection.commit()
    print("Tipo de ticket creado exitosamente")

def list_tipo_tickets(connection):
    cursor = connection.cursor()
    query = "SELECT * FROM tipo_ticket"
    cursor.execute(query)
    rows = cursor.fetchall()
    print("Lista de Tipos de Ticket:")
    for row in rows:
        print(f"Id: {row[0]}, Nombre: {row[1]}, ID Jefe: {row[2]}")

def update_tipo_ticket(connection):
    cursor = connection.cursor()
    tipo_ticket = int(input("Ingrese el ID del tipo de ticket que desea editar: "))
    nombre = input("Ingrese el nuevo nombre del ticket: ")
    id_jefe = int(input("Ingrese el nuevo ID del jefe: "))
    query = """
    UPDATE tipo_ticket 
    SET nombre = %s, id_jefe = %s 
    WHERE id_tipoticket = %s
    """
    cursor.execute(query, (nombre, id_jefe, tipo_ticket))
    connection.commit()
    print("Tipo de ticket actualizado exitosamente")

def delete_tipo_ticket(connection):
    cursor = connection.cursor()
    tipo_ticket = int(input("Ingrese el ID del tipo de ticket que desea eliminar: "))
    query = "DELETE FROM tipo_ticket WHERE id_tipoticket = %s"
    cursor.execute(query, (tipo_ticket,))
    connection.commit()
    print("Tipo de ticket eliminado exitosamente")

def menu_tipo_ticket():
    connection = create_connection()
    if not connection:
        return

    while True:
        print("\nGestión de Tipos de Ticket")
        print("1. Crear Tipo de Ticket")
        print("2. Listar Tipos de Ticket")
        print("3. Editar Tipo de Ticket")
        print("4. Eliminar Tipo de Ticket")
        print("5. Salir")

        choice = input("Seleccione una opción: ")

        if choice == '1':
            create_tipo_ticket(connection)
        elif choice == '2':
            list_tipo_tickets(connection)
        elif choice == '3':
            update_tipo_ticket(connection)
        elif choice == '4':
            delete_tipo_ticket(connection)
        elif choice == '5':
            break
        else:
            print("Opción no válida, intente de nuevo")

    close_connection(connection)

if __name__ == '__main__':
    main()
