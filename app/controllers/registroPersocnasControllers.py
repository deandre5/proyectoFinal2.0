from app.model.PersonasModel import Personas
import datetime
import bcrypt

personas = Personas()

class RegistroPersocnasControllers:

    def registrar(self,content):
        nombres = content.get('nombres')
        apellidos = content.get('apellidos')
        documento = content.get('documento')
        ficha = content.get('ficha')
        idprograma = content.get('idprograma')
        telefono = content.get('telefono')
        correo = content.get('correo')
        edad = content.get('edad')
        password = content.get('password')
        jornada = content.get('jornada')
        tipopersona = content.get('tipopersona')
        tipouser = content.get('tipouser')
        fecha = datetime.datetime.utcnow()

        try:
            salt = bcrypt.gensalt()
            hash_password = bcrypt.hashpw(
                bytes(str(password), encoding='utf-8'), salt)

            final_password = hash_password.decode()

            registro = personas.insert(nombres, apellidos, documento,ficha, idprograma,telefono,correo,edad,final_password, jornada, tipopersona, tipouser, fecha)

            if registro:
                return True
        
        except Exception as Error:
            return Error

        
    
    def consultar(self, content):
        documento = content.get('documento')
        correo = content.get('correo')

        consulta = personas.consult(documento,correo)

        return consulta 


