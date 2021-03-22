from app.model.PersonasModel import Personas
import bcrypt

personas = Personas()

class LoginPersonas:
    def login(self, content):
        
        password = content.get('password')
        correo = content.get('correo')

        login = personas.select(correo)

        diccionarios = {}

        if(login):
            for row in login:
                password_db = bytes(row[1], encoding='utf-8')
                correo = row[0]
                tipouser = row[2]
                idrutina = row[3]
                iddieta = row[4]
                idtest = row[5]
                documento = row[6]

                diccionarios['correo'] = correo
                diccionarios["user"] = tipouser
                diccionarios["rutina"] =idrutina
                diccionarios["dieta"] =iddieta
                diccionarios["test"] = idtest
                diccionarios["documento"] = documento

        

        if bcrypt.checkpw(bytes(str(password), encoding='utf-8'), password_db):
            return diccionarios

        else:
            return False



        