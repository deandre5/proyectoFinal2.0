from app.model.PersonasModel import Personas

personas = Personas


class CalcularImc():
    def calcular(self, content, documento):
        peso = int(content.get('peso'))
        altura = int(content.get('altura'))

        alturametro = altura/100

        altura2 = alturametro*alturametro

        imc = peso/altura2

        idTest = personas.consultImc()

        if idTest:
            for i in idTest:
                id_bd = i.get('id')+1
        # si no hay ejercicios registrados, este toma el valor de 1
        else:
            id_bd = 1

        registerTest = personas.registerTest(id_bd, peso, altura, imc)

        if (registerTest):

            consultPerson = personas.consult(documento)

            if (consultPerson):

                registerTestPerson = personas.registerTestPerson(
                    id_bd, documento)

                if (registerTestPerson):

                    return True
                else:
                    return False

            else:
                return "False"

        else:
            return False
