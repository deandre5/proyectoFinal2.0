import psycopg2


class Personas:

    def consult(documento, correo):
        try:
            conexion = psycopg2.connect(database="dd1o1liu6nsqob", user="gvjdpzhyjsvfxs", password="5ffbbd36b7bf7d3ff6e7edb572b8667da3b15d4396b445f4e705f13c25f8d075",
                                        host="ec2-52-23-190-126.compute-1.amazonaws.com", port="5432")

            cursor = conexion.cursor()

            sql = "SELECT * FROM personas WHERE documento = %s or correo = %s"

            cursor.execute(sql, (documento, correo,))
            diccionario = cursor.fetchall()
            conexion.commit()

            print(diccionario)

            # se examina el len del diccionario despues de la consulta, si es mayor a cero se devuelve true ya que se encuentra repetido

            if len(diccionario) > 0:
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

    def consultar(self):
        try:

            conexion = psycopg2.connect(database="dd1o1liu6nsqob", user="gvjdpzhyjsvfxs", password="5ffbbd36b7bf7d3ff6e7edb572b8667da3b15d4396b445f4e705f13c25f8d075",
                                        host="ec2-52-23-190-126.compute-1.amazonaws.com", port="5432")
            cursor = conexion.cursor()

            sql = "SELECT * FROM personas ORDER BY id ASC"
            cursor.execute(sql)
            diccionario = cursor.fetchall()
            diccionarios = []
            # for que nos permite crear un objeto items para luego añadirlo a una lista y devolver su contenido
            for item in diccionario:
                items = {"nombres": item[0], "apellidos": item[1],
                         "documento": item[2], "ficha": item[3], "idprograma": item[4], "telefono": item[5], "correo": item[6], "edad": item[7], "jornada": item[9], "tipopersona": item[10], "tipouser": item[11], "fecha": item[12], "idrutina": item[13], "iddieta": item[14], "imagen": item[15], "idtest": item[16]}

                diccionarios.append(items)
            conexion.commit()

        except Exception as error:
            print("Error in the conetion with the database", error)
        finally:
            cursor.close()
            conexion.close()
            print(diccionarios)
            return diccionarios

    def select(self, correo):
        try:
            conexion = psycopg2.connect(database="dd1o1liu6nsqob", user="gvjdpzhyjsvfxs", password="5ffbbd36b7bf7d3ff6e7edb572b8667da3b15d4396b445f4e705f13c25f8d075",
                                        host="ec2-52-23-190-126.compute-1.amazonaws.com", port="5432")

            cursor = conexion.cursor()
            sql = "SELECT correo, contraseña, tipopersona, idrutina, iddieta, idtest, documento, nombres FROM personas where correo = %s"
            cursor.execute(sql, (correo,))

            diccionario = cursor.fetchall()

            conexion.commit()
        except Exception as error:
            print("Error in the connection with the data base", error)
        finally:
            cursor.close()
            conexion.close()
            return diccionario

    def consultImc():
        try:

            conexion = psycopg2.connect(database="dd1o1liu6nsqob", user="gvjdpzhyjsvfxs", password="5ffbbd36b7bf7d3ff6e7edb572b8667da3b15d4396b445f4e705f13c25f8d075",
                                        host="ec2-52-23-190-126.compute-1.amazonaws.com", port="5432")
            cursor = conexion.cursor()

            sql = "SELECT * FROM test ORDER BY id_test ASC"
            cursor.execute(sql)
            diccionario = cursor.fetchall()
            diccionarios = []
            # for que nos permite crear un objeto items para luego añadirlo a una lista y devolver su contenido
            for item in diccionario:
                items = {"id": item[0], "peso": item[1],
                         "talla": item[2], "imc": item[3]}

                diccionarios.append(items)
            conexion.commit()

        except Exception as error:
            print("Error in the conetion with the database", error)
        finally:
            cursor.close()
            conexion.close()
            print(diccionarios)
            return diccionarios

    def registerTest(id, peso, talla, imc):
        try:
            conexion = psycopg2.connect(database="dd1o1liu6nsqob", user="gvjdpzhyjsvfxs", password="5ffbbd36b7bf7d3ff6e7edb572b8667da3b15d4396b445f4e705f13c25f8d075",
                                        host="ec2-52-23-190-126.compute-1.amazonaws.com", port="5432")

            cursor = conexion.cursor()

            sql = "INSERT INTO test VALUES(%s, %s, %s, %s)"
            datos = (id, peso, talla, imc)

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

    def registerTestPerson(idtest, documento):
        try:
            conexion = psycopg2.connect(database="dd1o1liu6nsqob", user="gvjdpzhyjsvfxs", password="5ffbbd36b7bf7d3ff6e7edb572b8667da3b15d4396b445f4e705f13c25f8d075",
                                        host="ec2-52-23-190-126.compute-1.amazonaws.com", port="5432")

            cursor = conexion.cursor()

            sql = "UPDATE personas SET idtest = %s WHERE documento = %s"

            documento = (documento)
            idtest = (idtest)

            cursor.execute(sql, (idtest, documento))
            conexion.commit()
            # si la actualizacion fue exitosa el status se vuelve true
            status = True

        except Exception as error:
            print("Error in the conetion with the database", error)
            # si hay error se convierte en false
            status = False
        finally:
            cursor.close()
            conexion.close()
            return status

    def consult(documento):
        try:
            conexion = psycopg2.connect(database="dd1o1liu6nsqob", user="gvjdpzhyjsvfxs", password="5ffbbd36b7bf7d3ff6e7edb572b8667da3b15d4396b445f4e705f13c25f8d075",
                                        host="ec2-52-23-190-126.compute-1.amazonaws.com", port="5432")

            cursor = conexion.cursor()

            sql = "SELECT * FROM personas WHERE documento = %s"

            cursor.execute(sql, (documento, ))
            diccionario = cursor.fetchall()
            conexion.commit()

            print(diccionario)

            # se examina el len del diccionario despues de la consulta, si es mayor a cero se devuelve true ya que se encuentra repetido

            if len(diccionario) > 0:
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

    def consultarTest(self):
        try:

            conexion = psycopg2.connect(database="dd1o1liu6nsqob", user="gvjdpzhyjsvfxs", password="5ffbbd36b7bf7d3ff6e7edb572b8667da3b15d4396b445f4e705f13c25f8d075",
                                        host="ec2-52-23-190-126.compute-1.amazonaws.com", port="5432")
            cursor = conexion.cursor()

            sql = "SELECT p.nombres, p.apellidos, p.documento, t.peso, t.talla, t.imc FROM test t, personas p WHERE p.idtest = t.id_test ORDER BY p.nombres, p.apellidos ASC"
            cursor.execute(sql)
            diccionario = cursor.fetchall()
            diccionarios = []
            # for que nos permite crear un objeto items para luego añadirlo a una lista y devolver su contenido
            for item in diccionario:
                items = {"nombres": item[0], "apellidos": item[1],
                         "documento": item[2], "peso": item[3], "talla": item[4], "imc": item[5]}

                diccionarios.append(items)
            conexion.commit()

        except Exception as error:
            print("Error in the conetion with the database", error)
        finally:
            cursor.close()
            conexion.close()
            print(diccionarios)
            return diccionarios

    def consultarTestID(self, id):
        try:
            conexion = psycopg2.connect(database="dd1o1liu6nsqob", user="gvjdpzhyjsvfxs", password="5ffbbd36b7bf7d3ff6e7edb572b8667da3b15d4396b445f4e705f13c25f8d075",
                                        host="ec2-52-23-190-126.compute-1.amazonaws.com", port="5432")
            cursor = conexion.cursor()

            sql = "SELECT * FROM test WHERE id_test = %s"
            cursor.execute(sql, (id, ))
            diccionario = cursor.fetchall()
            diccionarios = []
            # for que nos permite crear un objeto items para luego añadirlo a una lista y devolver su contenido
            for item in diccionario:
                items = {"id": item[0], "peso": item[1],
                         "talla": item[2], "imc": item[3]}

            diccionarios.append(items)

            conexion.commit()

        except Exception as error:
            print("Error in the conetion with the database", error)
        finally:
            print(diccionarios)
            cursor.close()
            conexion.close()
            return diccionarios

    def estadisticas(self):
        try:
            conexion = psycopg2.connect(database="dd1o1liu6nsqob", user="gvjdpzhyjsvfxs", password="5ffbbd36b7bf7d3ff6e7edb572b8667da3b15d4396b445f4e705f13c25f8d075",
                                        host="ec2-52-23-190-126.compute-1.amazonaws.com", port="5432")
            cursor = conexion.cursor()

            diccionarios = []

            sql = "SELECT count(*) FROM test"
            cursor.execute(sql,)
            diccionario = cursor.fetchall()
            test = diccionario[0]
            conexion.commit()

            sql = "SELECT count(*) FROM rutinas"
            cursor.execute(sql,)
            diccionario = cursor.fetchall()
            rutinas = diccionario[0]
            conexion.commit()

            sql = "SELECT count(*) FROM ejercicios"
            cursor.execute(sql,)
            diccionario = cursor.fetchall()
            ejercicios = diccionario[0]
            conexion.commit()

            sql = "SELECT count(*) FROM dietas"
            cursor.execute(sql,)
            diccionario = cursor.fetchall()
            dietas = diccionario[0]
            conexion.commit()

            sql = "SELECT count(*) FROM personas WHERE tipouser = 'admin'"
            cursor.execute(sql,)
            diccionario = cursor.fetchall()
            admin = diccionario[0]
            conexion.commit()

            sql = "SELECT count(*) FROM personas WHERE tipouser = 'user'"
            cursor.execute(sql,)
            diccionario = cursor.fetchall()
            user = diccionario[0]
            conexion.commit()

            sql = "SELECT count(*) FROM personas"
            cursor.execute(sql,)
            diccionario = cursor.fetchall()
            personas = diccionario[0]
            conexion.commit()

            items = {"test": test[0], "rutinas": rutinas[0], "ejercicios": ejercicios[0],
                     "dietas": dietas[0], "admin": admin[0], "user": user[0], "personas": personas[0]}

            diccionarios.append(items)

        except Exception as error:
            print("Error in the conetion with the database", error)
        finally:
            print(diccionarios)
            cursor.close()
            conexion.close()
            return diccionarios
