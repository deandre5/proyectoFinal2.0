from app.model.PersonasModel import Personas

personas = Personas()

class ConsultarTest():
    def consultar(self):

        consulta = personas.consultarTest()


        if (consulta):
            return consulta
        else:
            return False

    def consultarTestId(self, id):

        consulta = personas.consultarTestID(id)

        if (consulta):
            return consulta
        else:
            return False


        
