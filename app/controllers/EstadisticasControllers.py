from app.model.PersonasModel import Personas

personas = Personas()

class Estadisticas():
    def generarEstadisticas(self):

        estadisticas = personas.estadisticas()
        return estadisticas