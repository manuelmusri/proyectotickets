import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='tickets',
            user='root',
            password=''
        )
        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
            return connection
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def close_connection(connection):
    if connection.is_connected():
        connection.close()
        print("Conexión cerrada")

def create_area(connection):
    cursor = connection.cursor()
    nombre_area = input("Ingrese el nombre del área: ")
   
    activo = int(input("El área está activa? (1 para sí, 0 para no): "))
    query = "INSERT INTO area (nombre_area,activo) VALUES (%s,%s, %s)"
    cursor.execute(query, (nombre_area, activo))
    connection.commit()
    print("Área creada exitosamente")

def list_areas(connection):
    cursor = connection.cursor()
    query = "SELECT * FROM area"
    cursor.execute(query)
    rows = cursor.fetchall()
    print("Lista de Áreas:")
    for row in rows:
        print(f"ID: {row[0]}, Nombre: {row[1]}, Activo: {row[2]}")

def update_area(connection):
    cursor = connection.cursor()
    id_area = int(input("Ingrese el ID del área que desea editar: "))
    nombre_area = input("Ingrese el nuevo nombre del área: ")
   
    activo = int(input("El área está activa? (1 para sí, 0 para no): "))
    query = """
    UPDATE area 
    SET nombre_area = %s,  activo = %s 
    WHERE id_area = %s
    """
    cursor.execute(query, (nombre_area,activo, id_area))
    connection.commit()
    print("Área actualizada exitosamente")

def delete_area(connection):
    cursor = connection.cursor()
    id_area = int(input("Ingrese el ID del área que desea eliminar: "))
    query = "DELETE FROM area WHERE id_area = %s"
    cursor.execute(query, (id_area,))
    connection.commit()
    print("Área eliminada exitosamente")

def menu_crud_area():
    connection = create_connection()
    if not connection:
        return

    while True:
        print("\nGestión de Áreas")
        print("1. Crear Área")
        print("2. Listar Áreas")
        print("3. Editar Área")
        print("4. Eliminar Área")
        print("5. Salir")

        choice = input("Seleccione una opción: ")

        if choice == '1':
            create_area(connection)
        elif choice == '2':
            list_areas(connection)
        elif choice == '3':
            update_area(connection)
        elif choice == '4':
            delete_area(connection)
        elif choice == '5':
            break
        else:
            print("Opción no válida, intente de nuevo")

    close_connection(connection)

