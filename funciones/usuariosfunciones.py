import hashlib
from conexion.conexion import create_connection, close_connection

class ComandoDML:
    def __init__(self, cnx):
        self.__cnx = cnx
    
    def seleccionarUsers2(self):
        cursor = None
        try:
            sql = """SELECT a.id_usuario, a.nombre_usuario, a.apellido_usuario, a.pass_usuario, a.tel_usuario, a.correo_usuario, b.nombre_tipo 
                    FROM usuario a 
                    INNER JOIN tipo_usuario b on (a.id_tusuario = b.id_tusuario);"""
            cursor = self.__cnx.cursor()
            cursor.execute(sql)
            users = cursor.fetchall()
            print("Usuarios seleccionados: ", users)
            return users
        except Exception as ex:
            print("seleccionarTodosUsuarios -> {}".format(ex))
        finally:
            if cursor:
                cursor.close()

class MantenedorUsuarios:
    def __init__(self):
        self.__cnx = create_connection()
    
    def menu_users(self):
        connection = self.__cnx
        if not connection:
            return
        while True:
            print("""1. Crear Usuario Ejecutivo de Área
    2. Crear Usuario Ejecutivo de Mesa
    4. Modificar Usuario
    5. Eliminar Usuario
    6. Listar Usuarios
    0 salir""")
            opt1 = int(input("Ingrese Opción: "))
            if opt1 == 1:
                self.crear_usuario(connection, 2)  # 2  Jefe de Área
            elif opt1 == 2:
                self.crear_usuario(connection, 3)  # 3Ejecutivo de Mesa
            elif opt1 == 6:
                print("Listando Usuarios: ")
                print("-*-" * 25)
                comando_dml = ComandoDML(connection)  # Crear instancia de ComandoDML
                usuarios = comando_dml.seleccionarUsers2()  # Llamar al método en la instancia
                if usuarios:
                    for user in usuarios:
                        print("id: {} | Nombre: {} | Apellido: {} | Password (con MD5): {} | Teléfono Usuario: {} | Email Usuario: {} | Tipo usuario: {}".format(user[0], user[1], user[2], user[3], user[4], user[5], user[6]))
                else:
                    print("No se encontraron usuarios.")
            elif opt1 == 0:
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")
    
    def crear_usuario(self, connection, tipo_usuario):
        print("ADVERTENCIA: Una vez creado el usuario NO puede cambiar de categoría")
        print("Lo anterior a fin de mantener la integridad de la BD")
        
        nombreusr = input("Ingrese Nombre: ")
        apellidousr = input("Ingrese Apellido: ")
        correo = input("Ingrese Correo electrónico: ")
        telefono = input("Ingrese el teléfono del usuario (solo números): ")
        
        while not telefono.isdigit():
            print("El teléfono debe contener solo números.")
            telefono = input("Ingrese el teléfono del usuario (solo números): ")
        
        telefono = int(telefono)
        pwdusr = input("Ingrese Contraseña: ")
        md5pwd = hashlib.md5(pwdusr.encode()).hexdigest()

        self.crearjarea(connection, md5pwd, nombreusr, apellidousr, telefono, correo, tipo_usuario)
    
    def crearjarea(self, connection, md5pwd, nombre, apellido, telefono, mail, tipousr):
        cursor = None
        try:
            sql = """INSERT INTO usuario (pass_usuario, nombre_usuario, apellido_usuario, tel_usuario, correo_usuario, id_tusuario)
                        VALUES (%s, %s, %s, %s, %s, %s)"""
            val = (md5pwd, nombre, apellido, telefono, mail, tipousr)
            cursor = connection.cursor()
            cursor.execute(sql, val)
            connection.commit()
            if cursor.lastrowid:
                print("Usuario ingresado correctamente con ID:", cursor.lastrowid)
                return cursor.lastrowid
            else:
                print("No se pudo obtener el ID del último usuario insertado.")
        except Exception as ex:
            print("insertUsuario -> {}".format(ex))
        finally:
            if cursor:
                cursor.close()


