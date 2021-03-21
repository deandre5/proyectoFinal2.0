import psycopg2


class Anuncios():
    def consultar(self):
        try:

            conexion = psycopg2.connect(database="dd1o1liu6nsqob", user="gvjdpzhyjsvfxs", password="5ffbbd36b7bf7d3ff6e7edb572b8667da3b15d4396b445f4e705f13c25f8d075",
                                        host="ec2-52-23-190-126.compute-1.amazonaws.com", port="5432")
            cursor = conexion.cursor()

            sql = "SELECT * FROM anuncios ORDER BY id_anuncios ASC"
            cursor.execute(sql)
            diccionario = cursor.fetchall()
            diccionarios = []
            # for que nos permite crear un objeto items para luego añadirlo a una lista y devolver su contenido
            for item in diccionario:
                items = {"id": item[0], "titulo": item[1],
                         "descripcion": item[2], "imagen": str(item[3])}

                diccionarios.append(items)
            conexion.commit()

        except Exception as error:
            print("Error in the conetion with the database", error)
        finally:
            cursor.close()
            conexion.close()
            print(diccionarios)
            return diccionarios

    def insert(self, id, titulo, descripcion, imagen):
        try:
            conexion = psycopg2.connect(database="dd1o1liu6nsqob", user="gvjdpzhyjsvfxs", password="5ffbbd36b7bf7d3ff6e7edb572b8667da3b15d4396b445f4e705f13c25f8d075",
                                        host="ec2-52-23-190-126.compute-1.amazonaws.com", port="5432")

            cursor = conexion.cursor()

            sql = "INSERT INTO anuncios VALUES(%s, %s, %s, %s)"
            datos = (id, titulo, descripcion, imagen)

            cursor.execute(sql, datos)

            conexion.commit()

            status = True

        except Exception as error:
            print("Error in the conexion with the database", error)

            status = False

        finally:
            cursor.close()
            conexion.close()
            return status

    def consultarAnuncios(self, nombre):
        try:
            conexion = psycopg2.connect(database="dd1o1liu6nsqob", user="gvjdpzhyjsvfxs", password="5ffbbd36b7bf7d3ff6e7edb572b8667da3b15d4396b445f4e705f13c25f8d075",
                                        host="ec2-52-23-190-126.compute-1.amazonaws.com", port="5432")

            cursor = conexion.cursor()

            sql = "SELECT * FROM anuncios WHERE titulo = %s"

            cursor.execute(sql, (nombre,))
            diccionario = cursor.fetchall()
            conexion.commit()

            print(diccionario)

            # se examina el len del diccionario despues de la consulta, si es mayor a cero se devuelve true ya que se encuentra repetido

            if len(diccionario) > 1:
                status = True
            # caso contrario false
            else:
                status = False

        except Exception as error:
            print("Error in the conetion with the database", error)

            status = False

        finally:

            cursor.close()
            conexion.close()
            return status

    def ConsultaId(self, id):
        try:
            conexion = psycopg2.connect(database="dd1o1liu6nsqob", user="gvjdpzhyjsvfxs", password="5ffbbd36b7bf7d3ff6e7edb572b8667da3b15d4396b445f4e705f13c25f8d075",
                                        host="ec2-52-23-190-126.compute-1.amazonaws.com", port="5432")
            cursor = conexion.cursor()

            sql = "SELECT * FROM anuncios WHERE id_anuncios = %s"
            cursor.execute(sql, (id, ))
            diccionario = cursor.fetchall()
            diccionarios = []
            # for que nos permite crear un objeto items para luego añadirlo a una lista y devolver su contenido
            for item in diccionario:
                items = {"id": item[0], "titulo": item[1],
                         "descripcion": item[2], "imagen": str(item[3])}

            diccionarios.append(items)

            conexion.commit()

        except Exception as error:
            print("Error in the conetion with the database", error)
        finally:
            print(diccionarios)
            cursor.close()
            conexion.close()
            return diccionarios

    def remove(self, id):
        try:
            conexion = psycopg2.connect(database="dd1o1liu6nsqob", user="gvjdpzhyjsvfxs", password="5ffbbd36b7bf7d3ff6e7edb572b8667da3b15d4396b445f4e705f13c25f8d075",
                                        host="ec2-52-23-190-126.compute-1.amazonaws.com", port="5432")

            cursor = conexion.cursor()

            sql = "DELETE FROM anuncios WHERE id_anuncios = %s"

            cursor.execute(sql, (id,))
            conexion.commit()

        except Exception as error:
            print("Error in the connection with the database", error)

        finally:
            cursor.close()
            conexion.close()

    def actualizacion(self, id, titulo, descripcion, imagen):
        try:
            conexion = psycopg2.connect(database="dd1o1liu6nsqob", user="gvjdpzhyjsvfxs", password="5ffbbd36b7bf7d3ff6e7edb572b8667da3b15d4396b445f4e705f13c25f8d075",
                                        host="ec2-52-23-190-126.compute-1.amazonaws.com", port="5432")

            cursor = conexion.cursor()

            sql = "UPDATE anuncios SET titulo = %s, descripcion = %s, imagen = %s WHERE id_anuncios = %s "

            id = (id)
            titulo = (titulo)
            descripcion = (descripcion)
            imagen = (imagen)

            cursor.execute(sql, (titulo, descripcion, imagen, id))
            conexion.commit()
            status = True

        except Exception as error:
            print("Error in the conetion with the database", error)
            status = False
        finally:
            cursor.close()
            conexion.close()
            return status  
