import hashlib

class Login:
    def __init__(self, cnx):
        self.__cnx = cnx

    def verificar_usuario(self, nombre, contraseña):
        try:
            sql = """SELECT * FROM usuario WHERE nombre_usuario = %s AND pass_usuario = %s;"""
            hashed_password = hashlib.md5(contraseña.encode()).hexdigest()
            val = (nombre, hashed_password)
            cursor = self.__cnx.cursor()
            cursor.execute(sql, val)
            my_result = cursor.fetchone()
            cursor.close()
            
            # Logs de depuración
            print(f"Consulta ejecutada: {cursor.statement}")
            print(f"Resultado de la consulta para verificar_usuario: {my_result}")
            
            return my_result is not None
        except Exception as ex:
            print(f"verificar_usuario -> {ex}")
            return False


    def verificar_tipo(self, nombre):
        try:
            sql = """SELECT tipo.nombre_tipo FROM tipo_usuario tipo
                     JOIN usuario us ON us.id_tusuario = tipo.id_tusuario
                     WHERE us.nombre_usuario = %s;"""
            val = (nombre,)
            cursor = self.__cnx.cursor()
            cursor.execute(sql, val)
            my_result = cursor.fetchone()
            cursor.close()

            # Logs de depuración
            print(f"Consulta ejecutada: {cursor.statement}")
            print(f"Resultado de la consulta para verificar_tipo: {my_result}")
            
            if my_result is not None:
                tipo_usuario = my_result[0].lower()
                if tipo_usuario == "jefe de mesa":
                    return 1
                elif tipo_usuario == "ejecutivo de mesa":
                    return 2
                elif tipo_usuario == "ejecutivo de area":
                    return 3
            return None
        except Exception as ex:
            print(f"verificar_tipo -> {ex}")
            return None
