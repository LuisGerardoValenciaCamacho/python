import MySQLdb


class UsuariosDAO:

    @staticmethod
    def guardarUsuario(nombre=None, apellido=None, fechaNacimiento=None, genero=None, id=None):
        datos = ['localhost', 'root', '', 'Proyecto2']
        conn = MySQLdb.connect(*datos)
        cursor = conn.cursor()

        if nombre is None and apellido is None and fechaNacimiento is None and genero is None and id is None:
            cursor.execute("SELECT * FROM usuarios")
            data = cursor.fetchall()
            return data

        elif nombre is None and apellido is None and fechaNacimiento is None and genero is None and id is not None:
            print(id)
            cursor.execute("DELETE FROM usuarios WHERE id = {}".format(id))
            conn.commit()

        else:
            cursor.execute("INSERT INTO usuarios(nombre, apellidos, fecha_nacimiento, genero) VALUES (%s, %s, %s, %s)", (nombre, apellido, fechaNacimiento, genero))
            conn.commit()

        cursor.close()
        conn.close()
