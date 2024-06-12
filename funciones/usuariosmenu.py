


from conexion.conexion import create_connection, close_connection
from funciones.usuariosfunciones import ComandoDML
from funciones.usuariosfunciones import MantenedorUsuarios
import hashlib

cnx = create_connection()
DML = ComandoDML(cnx)
usuariosadmin = MantenedorUsuarios()




                